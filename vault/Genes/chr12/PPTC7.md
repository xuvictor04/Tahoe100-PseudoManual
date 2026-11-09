---
symbol: "PPTC7"
type: "gene"
col: 12293
ensembl_id: "ENSG00000196850"
name: "protein phosphatase targeting COQ7"
location: "12q24.11"
module: 182
arm: "+"
pooled_cpm: 67.15
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 17
n_dd_up_clean: 19
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# PPTC7

*protein phosphatase targeting COQ7* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.75× (z +21.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (none with an alert); the strongest is [[Filgotinib (drug)]] 0.05 µM: 0.751× (z -4.3, q 0.010, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDFIP1]] (+0.55, fdr 1e-05), [[ANKRD33B]] (+0.55, fdr 1e-05), [[PLEKHA1]] (+0.52, fdr 2e-05); moves opposite to [[GON4L]] (-0.52, fdr 6e-05), [[ZSCAN5A]] (-0.52, fdr 2e-05), [[TUT7]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 182]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.75×** | +21.5 | 0e+00 | 46/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.89×** | +15.9 | 0e+00 | 48/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.92×** | +15.2 | 0e+00 | 48/49 (HT-29, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +14.9 | 0e+00 | 47/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.58×** | +13.7 | 1e-40 | 44/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.34×** | +12.7 | 3e-35 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +11.9 | 1e-30 | 45/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +10.2 | 1e-22 | 35/49 (AsPC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.93×** | +9.9 | 3e-21 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.47×** | +9.8 | 1e-20 | 44/48 (LoVo, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +8.5 | 9e-16 | 33/48 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +8.4 | 3e-15 | 37/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.59×** | +7.0 | 1e-10 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.1 | 4e-08 | 28/50 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +6.0 | 1e-07 | 32/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.002 | 23/48 (NCI-H2347, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.002 | 21/48 (CFPAC-1, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, none with an alert; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 0.05 µM |  | **0.751×** | -4.3 | 0.010 | 29/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.775×** | -3.8 | 0.029 | 23/47 (NCI-H2347, A498, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.029 | 22/48 (NCI-H1792, SW1417, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.776×** | -3.7 | 0.029 | 25/48 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.782×** | -3.6 | 0.034 | 26/48 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.789×** | -3.6 | 0.034 | 20/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.039 | 19/49 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.066 | 20/48 (AsPC-1, RKO, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.066 | 16/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Proglumide (drug)]] 0.05 µM |  | **0.808×** | -3.2 | 0.066 | 16/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.066 | 16/48 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.809×** | -3.2 | 0.066 | 19/48 (SW 1088, NCI-H1573, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.079 | 12/48 (SW 1088, NCI-H1792, …) | two highest doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.084 | 16/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.084 | 16/48 (NCI-H460, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.1 | 10 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.41× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 4.64× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 50.8 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +30.3) | — |
| [[NCI-H1792 (line)]] | alt | 70.3 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.1) | — |
| [[SW480 (line)]] | alt | 51.1 | 9 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.91× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 37.2 | 8 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.51× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.4) | — |
| [[LoVo (line)]] | wt | 122 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 50.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.0) | — |
| [[KATO III (line)]] | alt | 49.6 | 7 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.14× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 73.8 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.55× (z +17.0) | — |
| [[SW 900 (line)]] | alt | 55.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.6) | — |
| [[SW48 (line)]] | wt | 98.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 50.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +13.6) | — |
| [[C32 (line)]] | wt | 85.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 45.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +18.7) | — |
| [[SNU-423 (line)]] | alt | 37.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +14.9) | — |
| [[H4 (line)]] | wt | 40.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.4) | — |
| [[A498 (line)]] | wt | 72.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +15.8) | — |
| [[A549 (line)]] | wt | 77.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +19.9) | — |
| [[AsPC-1 (line)]] | alt | 150 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 37.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +15.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.74× (z +10.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 4.74× (z +10.0) | — |
| [[A-172 (line)]] | wt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +18.1) | — |
| [[HS-578T (line)]] | alt | 60.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +15.1) | — |
| [[hTERT-HPNE (line)]] | wt | 55.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 127 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.98× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 11.1× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 75.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.13× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.6) | — |
| [[A-427 (line)]] | wt | 39.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.3) | — |
| [[COLO 205 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.43× (z +9.3) ⚠ toxic | — |
| [[HCT15 (line)]] | alt | 41.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 53.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.6) | — |
| [[J82 (line)]] | alt | 56.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 63.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.2) | — |
| [[RKO (line)]] | wt | 71.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 52.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.77× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDFIP1]] | +0.55 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ANKRD33B]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHA1]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[CYB5A]] | +0.52 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SPATA5L1]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[MAP3K8]] | +0.52 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ANXA4]] | +0.52 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[CHASERR]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[RAB21]] | +0.50 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[KDM1A]] | +0.50 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SNRPA1]] | +0.49 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[IFNGR2]] | +0.49 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GON4L]] | -0.52 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[ZSCAN5A]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TUT7]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SETX]] | -0.50 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[RRP7BP-1]] | -0.50 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[MZF1]] | -0.46 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TVP23C-CDRT4]] | -0.46 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[PILRB]] | -0.46 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[SDHAF2]] | -0.46 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[MIER2]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ZNF274]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MRFAP1]] | -0.45 | -0.50 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (3.0, -25.0); signed map (35.9, -24.3). **Vector** length 76.4, 22.8% of its response variance represented; |z| ≥ 3 in 1,390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +4.6 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.6 | +11.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.0 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | +15.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | +0.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase targeting COQ7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,533,245-110,583,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TA-PP2C |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI37](https://www.uniprot.org/uniprotkb/Q8NI37) (Protein phosphatase PTC7 homolog):

> Protein phosphatase that plays an essential role in mitochondrial metabolism and biogenesis. Positively regulates biosynthesis of the ubiquinone, coenzyme Q. Dephosphorylates the ubiquinone biosynthesis protein COQ7 which is likely to lead to its activation. Serves as a crucial sensor for mitophagy, though the underlying mechanism remains ambiguous (By similarity). May dephosphorylate BNIP3 and NIX and thereby directly regulates mitophagy receptor function and stability (By similarity). …

**Summary**, from NCBI Gene [160760](https://www.ncbi.nlm.nih.gov/gene/160760):

> Enables protein serine/threonine phosphatase activity and protein-macromolecule adaptor activity. Involved in negative regulation of mitophagy and positive regulation of ubiquinone biosynthetic process. Located in mitochondrial matrix. Is active in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30695) · Entrez [160760](https://www.ncbi.nlm.nih.gov/gene/160760) · UniProt [Q8NI37](https://www.uniprot.org/uniprotkb/Q8NI37) · Ensembl [ENSG00000196850](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196850)

## Data

Gene col 12293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12293); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12293]; `tensor/DDL_lfc|DDL_z.npy` [12293]; `embed/gene_vectors.npy` [12293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12293 or target_col == 12293). Every well: [[PPTC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPTC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
