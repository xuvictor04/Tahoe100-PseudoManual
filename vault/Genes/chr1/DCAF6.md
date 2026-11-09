---
symbol: "DCAF6"
type: "gene"
col: 6689
ensembl_id: "ENSG00000143164"
name: "DDB1 and CUL4 associated factor 6"
location: "1q24.2"
module: 1
arm: "-"
pooled_cpm: 212.27
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DCAF6

*DDB1 and CUL4 associated factor 6* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.22× (z +5.0, q 3e-04, up in 29 of 49 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Binimetinib (drug)]] 5 µM: 1.17× (z +3.9, q 0.015, up in 16 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.19×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (18 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.455× (z -19.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD9]] (+0.63, fdr 1e-05), [[LCA5]] (+0.63, fdr 2e-05), [[MPC2]] (+0.62, fdr 1e-05, ⚠ same locus), [[ATF2]] (+0.62, fdr 7e-06); moves opposite to [[ZNF195]] (-0.59, fdr 1e-05), [[WDR4]] (-0.58, fdr 1e-05), [[ZNF202]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6689.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.19×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.22×** | +5.0 | 3e-04 | 29/49 (A-172, SHP-77, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.22×** | +4.8 | 4e-04 | 30/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.9 | 0.015 | 16/49 (SW480, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.9 | 0.015 | 18/47 (RPMI-7951, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.8 | 0.018 | 11/48 (AsPC-1, A-172, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.020 | 24/48 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.032 | 11/48 (NCI-H2347, HS-578T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.15× | +3.5 | 0.033 | 13/50 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.041 | 21/50 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.3 | 0.052 | 0/50 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.052 | 15/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.070 | 15/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.1 | 0.098 | 5/48 (SW480, A-427, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 25 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.455×** | -19.7 | 0e+00 | 47/48 (SW480, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -15.7 | 0e+00 | 44/47 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.530×** | -14.7 | 0e+00 | 41/45 (NCI-H460, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.608×** | -12.4 | 3e-33 | 41/49 (NCI-H460, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.602×** | -12.2 | 3e-32 | 37/44 (NCI-H460, SW 900, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.711×** | -12.1 | 2e-31 | 32/48 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.622×** | -11.9 | 1e-30 | 41/48 (NCI-H23, NCI-H1792, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.684×** | -9.5 | 2e-19 | 37/48 (NCI-H1792, SNU-423, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.691×** | -8.9 | 4e-17 | 43/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.514×** | -8.7 | 2e-16 | 39/49 (SW 900, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.710×** | -8.6 | 6e-16 | 39/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.730×** | -7.9 | 2e-13 | 41/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.747×** | -7.3 | 1e-11 | 32/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.750×** | -7.2 | 3e-11 | 31/48 (SW 900, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.768×** | -6.6 | 2e-09 | 36/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.632×** | -6.0 | 6e-08 | 38/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.675×** | -5.1 | 7e-06 | 36/49 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.686×** | -4.9 | 2e-05 | 34/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.690×** | -4.9 | 3e-05 | 32/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.722×** | -4.2 | 5e-04 | 28/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.844× | -3.9 | 0.002 | 18/47 (HepG2/C3A, SW48, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.766×** | -3.5 | 0.008 | 20/47 (SW48, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.769×** | -3.4 | 0.010 | 24/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.823×** | -3.1 | 0.031 | 14/49 (MIA PaCa-2, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.891× | -2.9 | 0.059 | 13/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.888× | -2.8 | 0.064 | 10/48 (SW480, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 321 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -17.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.459× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 228 | 0 | 12 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -15.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -10.6) |
| [[SW 900 (line)]] | alt | 268 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.329× (z -15.9) |
| [[SW480 (line)]] | alt | 156 | 0 | 9 (8 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.297× (z -22.2) |
| [[MIA PaCa-2 (line)]] | alt | 383 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.337× (z -17.1) |
| [[NCI-H2030 (line)]] | alt | 238 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.396× (z -11.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 285 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.461× (z -12.8) |
| [[A-172 (line)]] | wt | 345 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -18.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.379× (z -16.1) |
| [[hTERT-HPNE (line)]] | wt | 270 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 246 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.395× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 206 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -21.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -19.0) |
| [[C32 (line)]] | wt | 190 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.346× (z -12.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.412× (z -11.1) |
| [[HOP62 (line)]] | alt | 215 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.455× (z -11.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -11.1) |
| [[J82 (line)]] | alt | 212 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -12.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 260 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.438× (z -12.7) |
| [[SNU-423 (line)]] | alt | 251 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.356× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 163 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -9.6) |
| [[HS-578T (line)]] | alt | 222 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.396× (z -14.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.562× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 161 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.450× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 242 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.379× (z -12.5) |
| [[SNU-1 (line)]] | wt | 233 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.289× (z -14.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.325× (z -14.0) |
| [[A498 (line)]] | wt | 241 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.495× (z -11.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.553× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 230 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.384× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.432× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 208 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.455× (z -11.7) |
| [[A-427 (line)]] | wt | 259 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.449× (z -12.7) |
| [[A549 (line)]] | wt | 198 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -20.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[BT-474 (line)]] | alt | 229 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.349× (z -13.3) |
| [[H4 (line)]] | wt | 203 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.436× (z -9.7) |
| [[HT-29 (line)]] | alt | 174 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.326× (z -17.7) |
| [[HCT15 (line)]] | alt | 263 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -12.1) |
| [[Hs 766T (line)]] | wt | 197 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.470× (z -9.7) |
| [[LS 180 (line)]] | wt | 171 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.497× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.549× (z -9.0) |
| [[PANC-1 (line)]] | alt | 221 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.550× (z -11.8) |
| [[RKO (line)]] | wt | 125 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.380× (z -11.8) |
| [[SW1417 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.553× (z -8.6) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 205 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.427× (z -10.0) |
| [[KATO III (line)]] | alt | 97.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SHP-77 (line)]] | alt | 109 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.470× (z -8.7) |
| [[SW48 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 205 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 171 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD9]] | +0.63 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[LCA5]] | +0.63 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[MPC2]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ATF2]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 | same gene group |
| [[RNASE4]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SEPTIN7]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ARL3]] | +0.58 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[FGFR1OP2]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[KDM3A]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RAB8B]] | +0.56 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ZMYM2]] | +0.56 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SKAP2]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[ELF2]] | +0.55 | +0.57 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF195]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[WDR4]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 | same gene group |
| [[ZNF202]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PUS1]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[MAK16]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.57 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[GRWD1]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 | same gene group |
| [[DCTD]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[GNL3L]] | -0.55 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ARMC6]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[CPSF7]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[LSG1]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.3, -37.5); signed map (-24.4, 17.0). **Vector** length 97.6, 32.5% of its response variance represented; |z| ≥ 3 in 1,473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.5 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.6 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.1 | +4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.4 | -19.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.0 | -15.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.6 | -8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -6.0 | -14.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -8.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:167,935,783-168,075,843 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC326; previously IQWD1 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors; MicroRNA protein coding host genes |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q58WW2](https://www.uniprot.org/uniprotkb/Q58WW2) (DDB1- and CUL4-associated factor 6):

> Ligand-dependent coactivator of nuclear receptors. Enhance transcriptional activity of the nuclear receptors NR3C1 and AR. May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [55827](https://www.ncbi.nlm.nih.gov/gene/55827):

> The protein encoded by this gene is a ligand-dependent coactivator of nuclear receptors, including nuclear receptor subfamily 3 group C member 1 (NR3C1), glucocorticoid receptor (GR), and androgen receptor (AR). The encoded protein and DNA damage binding protein 2 (DDB2) may act as tumor promoters and tumor suppressors, respectively, by regulating the level of androgen receptor in prostate tissues. In addition, this protein can act with glucocorticoid receptor to promote human papillomavirus …

**Accessions** — [HGNC:30002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30002) · Entrez [55827](https://www.ncbi.nlm.nih.gov/gene/55827) · UniProt [Q58WW2](https://www.uniprot.org/uniprotkb/Q58WW2) · Ensembl [ENSG00000143164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143164)

## Data

Gene col 6689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6689); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6689]; `tensor/DDL_lfc|DDL_z.npy` [6689]; `embed/gene_vectors.npy` [6689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6689 or target_col == 6689). Every well: [[DCAF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
