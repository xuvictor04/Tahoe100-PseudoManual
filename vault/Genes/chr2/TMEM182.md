---
symbol: "TMEM182"
type: "gene"
col: 9949
ensembl_id: "ENSG00000170417"
name: "transmembrane protein 182"
location: "2q12.1"
module: 56
arm: "+"
pooled_cpm: 33.03
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 35
n_dd_up_clean: 14
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TMEM182

*transmembrane protein 182* — 2q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.47× (z +8.8, q 6e-16, up in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.70× (z +8.5, q 4e-15, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.267× (z -29.9, q 0e+00, down in 43 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.211× (z -24.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUS1]] (+0.68, fdr 1e-05), [[CSNK2A1]] (+0.67, fdr 2e-05), [[EDEM2]] (+0.63, fdr 2e-05); moves opposite to [[CYTH2]] (-0.55, fdr 2e-04), [[WBP4]] (-0.52, fdr 1e-04), [[DDX5]] (-0.52, fdr 1e-04).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.47×** | +8.8 | 6e-16 | 35/47 (A-427, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +8.5 | 4e-15 | 34/47 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +7.7 | 4e-12 | 35/47 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.1 | 5e-05 | 25/47 (A498, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +4.5 | 6e-04 | 22/47 (AsPC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.002 | 22/47 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.003 | 14/47 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +4.0 | 0.004 | 22/47 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.006 | 15/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.020 | 15/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.022 | 16/46 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.022 | 16/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.24×** | +3.5 | 0.022 | 7/47 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.032 | 15/47 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.041 | 9/47 (HEC-1-A, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.041 | 10/47 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.057 | 7/47 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.062 | 6/47 (NCI-H1573, HS-578T, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.267×** | -29.9 | 0e+00 | 43/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.211×** | -24.9 | 0e+00 | 47/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.247×** | -22.4 | 0e+00 | 45/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.268×** | -20.3 | 0e+00 | 46/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.330×** | -17.7 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.338×** | -17.3 | 0e+00 | 45/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.405×** | -14.5 | 1e-45 | 39/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.481×** | -11.7 | 1e-29 | 40/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.485×** | -11.6 | 4e-29 | 38/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.566×** | -9.1 | 6e-18 | 33/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.603×** | -7.8 | 4e-13 | 31/46 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -7.6 | 1e-12 | 34/47 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.626×** | -6.9 | 2e-10 | 20/40 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.640×** | -6.7 | 8e-10 | 29/47 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.497×** | -5.8 | 2e-07 | 27/47 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.752×** | -4.5 | 2e-04 | 23/46 (CFPAC-1, HT-29, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.828×** | -4.2 | 7e-04 | 21/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.760×** | -4.0 | 0.001 | 23/46 (BT-474, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.783×** | -3.9 | 0.002 | 21/47 (LoVo, J82, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.645×** | -3.7 | 0.005 | 18/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.6 | 0 | 14 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -15.1) |
| [[PANC-1 (line)]] | alt | 39.1 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -34.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -22.9) |
| [[SW480 (line)]] | alt | 40.0 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -24.4) |
| [[A498 (line)]] | wt | 42.9 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -21.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -15.2) |
| [[LoVo (line)]] | wt | 45.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -20.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -18.2) |
| [[H4 (line)]] | wt | 65.7 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0385× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 96.0 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -23.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 35.2 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0575× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 57.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -22.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -10.8) |
| [[SW1417 (line)]] | alt | 36.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -22.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -15.4) |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -15.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.129× (z -13.3) |
| [[KATO III (line)]] | alt | 29.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0715× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 58.4 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0955× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -14.5) |
| [[A-427 (line)]] | wt | 22.8 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -9.5) |
| [[COLO 205 (line)]] | alt | 64.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -21.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0891× (z -18.5) |
| [[LS 180 (line)]] | wt | 47.2 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0887× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 36.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -13.2) |
| [[RKO (line)]] | wt | 31.7 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0838× (z -15.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.132× (z -12.8) |
| [[CHP-212 (line)]] | wt | 34.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0356× (z -13.1) |
| [[HCT15 (line)]] | alt | 41.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -13.7) |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 27.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0817× (z -16.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 21.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -17.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.246× (z -9.4) |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -10.4) |
| [[J82 (line)]] | alt | 15.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -15.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -10.9) |
| [[SHP-77 (line)]] | alt | 38.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -11.4) |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0759× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 22.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -15.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -10.4) |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -11.3) |
| [[C32 (line)]] | wt | 20.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.240× (z -10.4) |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[ETC-206 (drug)]] 0.05 µM 0.132× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 40.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.191× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0903× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -14.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 28.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -9.4) |
| [[SW 1271 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 5.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUS1]] | +0.68 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.67 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[EDEM2]] | +0.63 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[USPL1]] | +0.61 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[PRRC1]] | +0.61 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[EIF2A]] | +0.60 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.59 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CLINT1]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[DUXAP9]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[OSTC]] | +0.58 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[SHQ1]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH2]] | -0.55 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[WBP4]] | -0.52 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[DDX5]] | -0.52 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ZBED5]] | -0.52 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[MDGA1]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZFYVE16]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ARHGEF40]] | -0.51 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ERF]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[LETM2]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LRRC57]] | -0.49 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[SLC66A1]] | -0.49 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.1, -19.8); signed map (-43.8, 7.8). **Vector** length 79.1, 20.0% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +4.7 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +1.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +8.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.7 | -29.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.1 | -20.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.2 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 182 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.1 — chr2:102,736,905-103,019,900 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30294 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZP80](https://www.uniprot.org/uniprotkb/Q6ZP80) (Transmembrane protein 182):

> Negatively regulates myogenesis and skeletal muscle regeneration via its association with ITGB1 (By similarity). Modulates ITGB1 activation by decreasing ITGB1-LAMB1 interaction and inhibiting ITGB1-mediated intracellular signaling during myogenesis (By similarity).

**Summary**, from NCBI Gene [130827](https://www.ncbi.nlm.nih.gov/gene/130827):

> Predicted to be involved in myotube cell development involved in skeletal muscle regeneration; negative regulation of myoblast differentiation; and negative regulation of myoblast fusion. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26391) · Entrez [130827](https://www.ncbi.nlm.nih.gov/gene/130827) · UniProt [Q6ZP80](https://www.uniprot.org/uniprotkb/Q6ZP80) · Ensembl [ENSG00000170417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170417)

## Data

Gene col 9949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9949); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9949]; `tensor/DDL_lfc|DDL_z.npy` [9949]; `embed/gene_vectors.npy` [9949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9949 or target_col == 9949). Every well: [[TMEM182 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM182.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
