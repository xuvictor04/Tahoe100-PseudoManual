---
symbol: "SLC20A1"
type: "gene"
col: 6848
ensembl_id: "ENSG00000144136"
name: "solute carrier family 20 member 1"
location: "2q14.1"
module: 174
arm: "+"
pooled_cpm: 125.0
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 30
n_dd_up_clean: 15
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# SLC20A1

*solute carrier family 20 member 1* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.31× (z +14.2, q 6e-43, up in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.92× (z +11.5, q 4e-28, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.600× (z -9.1, q 6e-17, down in 36 of 50 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPCAL1]] (+0.72, fdr 7e-06), [[PTPN12]] (+0.67, fdr 7e-06), [[PHC2]] (+0.63, fdr 7e-06); moves opposite to [[PHC3]] (-0.55, fdr 3e-05), [[VDAC1P8]] (-0.50, fdr 3e-05), [[AIMP1]] (-0.49, fdr 4e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SMOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +14.2 | 6e-43 | 44/47 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.92×** | +11.5 | 4e-28 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.89×** | +11.2 | 5e-27 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +11.2 | 1e-26 | 35/48 (A498, COLO 205, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.82×** | +10.6 | 4e-24 | 38/48 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.74×** | +9.8 | 1e-20 | 33/48 (SNU-423, HCT15, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.72×** | +9.5 | 1e-19 | 37/48 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +8.6 | 5e-16 | 30/48 (A-172, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.55×** | +7.7 | 6e-13 | 30/48 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.55×** | +7.7 | 6e-13 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +7.3 | 1e-11 | 34/48 (SW48, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +7.2 | 3e-11 | 31/48 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +7.1 | 7e-11 | 38/48 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.7 | 6e-07 | 28/48 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.6 | 1e-06 | 26/48 (NCI-H2347, SW48, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.8 | 4e-05 | 28/48 (COLO 205, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.8 | 5e-05 | 26/49 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 9e-04 | 20/49 (NCI-H2347, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 23/48 (LS 180, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.023 | 17/48 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.031 | 16/49 (NCI-H1573, SW48, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.036 | 15/49 (SNU-423, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.056 | 11/48 (SNU-423, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6848.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.600×** | -9.1 | 6e-17 | 36/50 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.644×** | -8.1 | 1e-13 | 36/49 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.683×** | -7.8 | 1e-12 | 35/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.699×** | -7.7 | 1e-12 | 35/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.642×** | -7.5 | 7e-12 | 34/47 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.650×** | -7.3 | 3e-11 | 36/48 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.748×** | -7.2 | 4e-11 | 27/48 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.670×** | -7.0 | 1e-10 | 32/49 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.771×** | -6.2 | 3e-08 | 28/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.711×** | -6.0 | 1e-07 | 31/47 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.708×** | -5.8 | 3e-07 | 23/43 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.785×** | -5.7 | 6e-07 | 29/49 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.571×** | -5.2 | 1e-05 | 24/47 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.750×** | -5.0 | 2e-05 | 27/48 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -4.9 | 3e-05 | 26/49 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.743×** | -4.8 | 5e-05 | 26/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.607×** | -4.6 | 1e-04 | 24/50 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 174 | 0 | 12 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.233× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 315 | 1 | 10 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.55× (z +9.1) | [[Adagrasib (drug)]] 0.05 µM 0.317× (z -30.0) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 165 | 9 (6 ⚠) | 1 | [[Digitoxin (drug)]] 0.5 µM 7.08× (z +22.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.9) |
| [[SNU-423 (line)]] | alt | 75.0 | 8 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.30× (z +13.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 4.39× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 70.9 | 6 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.62× (z +11.8) | — |
| [[J82 (line)]] | alt | 94.1 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +12.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.94× (z +11.5) | — |
| [[SW480 (line)]] | alt | 146 | 6 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.62× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 144 | 5 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 10.3× (z +12.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 9.00× (z +12.1) | — |
| [[H4 (line)]] | wt | 111 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.57× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 140 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.477× (z -19.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 162 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.89× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 94.1 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.54× (z +11.0) | — |
| [[A-172 (line)]] | wt | 131 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +20.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.94× (z +9.8) | — |
| [[C32 (line)]] | wt | 83.0 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.92× (z +11.8) | [[Binimetinib (drug)]] 5 µM 0.283× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 106 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +20.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.99× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 58.0 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +9.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.68× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 158 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +9.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.87× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 152 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 3.80× (z +11.7) | [[Trametinib (drug)]] 5 µM 0.394× (z -9.1) |
| [[SHP-77 (line)]] | alt | 67.0 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.40× (z +11.5) ⚠ toxic | — |
| [[SW48 (line)]] | wt | 192 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.78× (z +11.2) | — |
| [[A498 (line)]] | wt | 96.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +18.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.40× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 309 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.70× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 70.2 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.19× (z +9.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 157 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.07× (z +8.8) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 8.01× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 163 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.75× (z +9.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.23× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 88.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.16× (z +8.5) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 241 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 2.83× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.7) |
| [[SW1417 (line)]] | alt | 291 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 48.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.62× (z +8.7) ⚠ toxic | — |
| [[AN3 CA (line)]] | alt | 72.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.27× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 62.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.91× (z +8.6) ⚠ unreliable plate only | — |
| [[LoVo (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 147 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.347× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.639× (z -10.8) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.588× (z -13.5) ⚠ position not correctable |
| [[A549 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 232 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPCAL1]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[PTPN12]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PHC2]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[DUSP5]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SPRY4]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SH2B3]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PLXNA1]] | +0.59 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[EML4]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RGS17]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ETV4]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC3]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[VDAC1P8]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[AIMP1]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PIGP]] | -0.49 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[TBC1D23]] | -0.49 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[COPZ1]] | -0.48 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[SYNRG]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMOX]] | B | SMOX activity raises SLC20A1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without SMOX | 0.048 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[SH3TC2-DT]] | B | SH3TC2-DT activity raises SLC20A1's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.44× lower at baseline in the lines without SH3TC2-DT | 0.083 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[MAP2K1]] | B | MAP2K1 activity raises SLC20A1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.2, 4.9); signed map (7.0, 48.4). **Vector** length 129, 42.6% of its response variance represented; |z| ≥ 3 in 1,787 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.6 | +14.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.0 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.0 | +9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.7 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.8 | -9.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.2 | -7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.3 | -7.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.2 | -8.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.2 | -7.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.9 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 20 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,645,939-112,663,825 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PiT-1, Glvr-1, PiT1; previously GLVR1 |
| Gene groups (HGNC) | Solute carrier family 20 |
| Hallmark sets | TGF_BETA_SIGNALING, APOPTOSIS |
| Reactome | 4 pathways, smallest: Sodium-coupled phosphate cotransporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUM9](https://www.uniprot.org/uniprotkb/Q8WUM9) (Sodium-dependent phosphate transporter 1):

> Sodium-phosphate symporter which preferentially transports the monovalent form of phosphate with a stoichiometry of two sodium ions per phosphate ion. May play a role in extracellular matrix and cartilage calcification as well as in vascular calcification. Essential for cell proliferation but this function is independent of its phosphate transporter activity.; (Microbial infection) May function as a retroviral receptor as it confers human cells susceptibility to infection to Gibbon Ape Leukemia …

**Summary**, from NCBI Gene [6574](https://www.ncbi.nlm.nih.gov/gene/6574):

> The protein encoded by this gene is a sodium-phosphate symporter that absorbs phosphate from interstitial fluid for use in cellular functions such as metabolism, signal transduction, and nucleic acid and lipid synthesis. The encoded protein is also a retroviral receptor, causing human cells to be susceptible to infection by gibbon ape leukemia virus, simian sarcoma-associated virus, feline leukemia virus subgroup B, and 10A1 murine leukemia virus.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:10946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10946) · Entrez [6574](https://www.ncbi.nlm.nih.gov/gene/6574) · UniProt [Q8WUM9](https://www.uniprot.org/uniprotkb/Q8WUM9) · Ensembl [ENSG00000144136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144136)

## Data

Gene col 6848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6848); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6848]; `tensor/DDL_lfc|DDL_z.npy` [6848]; `embed/gene_vectors.npy` [6848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6848 or target_col == 6848). Every well: [[SLC20A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC20A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
