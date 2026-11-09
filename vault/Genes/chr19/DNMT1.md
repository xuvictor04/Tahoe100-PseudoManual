---
symbol: "DNMT1"
type: "gene"
col: 5133
ensembl_id: "ENSG00000130816"
name: "DNA methyltransferase 1"
location: "19p13.2"
module: 6
arm: "+"
pooled_cpm: 92.11
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DNMT1

*DNA methyltransferase 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.97× (z +22.5, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.29× (z +4.0, q 0.002, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H23 5.20×, NCI-H1792 7.37×, HS-578T 4.48×, SW480 3.60×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (J82 3.01×, HS-578T 3.43×, A549 4.44×, NCI-H1792 3.71×, …; ⚠ cell-cycle shift, explains ~66% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.616× (z -11.2, q 3e-26, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -7.4, q 3e-11, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMC1A]] (+0.82, fdr 7e-06), [[HELLS]] (+0.78, fdr 7e-06), [[SKA3]] (+0.77, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 21 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5133.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H23 5.20×, NCI-H1792 7.37×, HS-578T 4.48×, SW480 3.60×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (J82 3.01×, HS-578T 3.43×, A549 4.44×, NCI-H1792 3.71×, …; ⚠ cell-cycle shift, explains ~66% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **3.97×** | +22.5 | 0e+00 | 49/49 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **3.24×** | +18.5 | 0e+00 | 42/42 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.82×** | +15.7 | 0e+00 | 44/45 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.83×** | +14.0 | 2e-42 | 37/48 (J82, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.20×** | +12.4 | 4e-33 | 45/48 (J82, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.78×** | +9.4 | 5e-19 | 39/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.71×** | +8.4 | 2e-15 | 42/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.66×** | +8.3 | 7e-15 | 40/48 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.59×** | +7.6 | 2e-12 | 40/48 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.48×** | +6.4 | 9e-09 | 33/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +6.2 | 2e-08 | 32/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +5.8 | 4e-07 | 30/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.42×** | +5.8 | 4e-07 | 31/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +5.6 | 8e-07 | 26/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | **1.39×** | +5.4 | 2e-06 | 30/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.002 | 23/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.20× | +2.9 | 0.081 | 17/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.616×** | -11.2 | 3e-26 | 45/48 (A498, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -7.4 | 3e-11 | 29/48 (NCI-H23, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.677×** | -6.4 | 4e-08 | 33/48 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.788×** | -5.5 | 6e-06 | 31/48 (HCT15, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.668×** | -5.2 | 2e-05 | 28/48 (A-427, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.694×** | -4.7 | 2e-04 | 32/50 (A-427, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.818×** | -4.6 | 3e-04 | 24/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.786×** | -4.5 | 6e-04 | 29/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.691×** | -4.3 | 0.001 | 24/48 (SW480, HCT15, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.779×** | -4.1 | 0.003 | 28/49 (NCI-H23, A498, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.785×** | -3.9 | 0.004 | 25/47 (LS 180, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.717×** | -3.9 | 0.005 | 23/48 (NCI-H23, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.846× | -3.9 | 0.005 | 21/49 (RKO, HEC-1-A, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.847× | -3.8 | 0.005 | 19/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.785×** | -3.8 | 0.006 | 25/47 (A-427, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.790×** | -3.7 | 0.008 | 21/47 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.579×** | -3.4 | 0.018 | 21/50 (A-427, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.026 | 16/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.811×** | -3.2 | 0.039 | 19/48 (NCI-H23, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.819×** | -3.1 | 0.042 | 19/48 (A-427, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.856× | -3.1 | 0.047 | 17/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.814×** | -3.0 | 0.066 | 20/49 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.800×** | -2.9 | 0.089 | 16/49 (Hs 766T, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 159 | 3 (3 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Selinexor (drug)]] 5 µM 0.374× (z -17.7) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.6) |
| [[HOP62 (line)]] | alt | 58.5 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[PANC-1 (line)]] | alt | 95.8 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SW480 (line)]] | alt | 122 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[HS-578T (line)]] | alt | 93.0 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +18.8) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H1792 (line)]] | alt | 44.1 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.37× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SW 900 (line)]] | alt | 77.5 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[A549 (line)]] | wt | 49.0 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +16.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[J82 (line)]] | alt | 139 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +20.2) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[LOX-IMVI (line)]] | wt | 56.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SHP-77 (line)]] | alt | 240 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.7) ⚠ cell-cycle shift, explains ~66% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.9) |
| [[SNU-423 (line)]] | alt | 60.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.94× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[A-172 (line)]] | wt | 93.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.8) ⚠ cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 5 µM 0.439× (z -10.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-427 (line)]] | wt | 162 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Selinexor (drug)]] 5 µM 0.374× (z -14.9) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -10.0) |
| [[C32 (line)]] | wt | 148 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Selinexor (drug)]] 5 µM 0.322× (z -15.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 36.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[H4 (line)]] | wt | 55.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.11× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | [[Selinexor (drug)]] 5 µM 0.349× (z -8.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LoVo (line)]] | wt | 51.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.84× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | [[Selinexor (drug)]] 5 µM 0.509× (z -9.1) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LS 180 (line)]] | wt | 73.5 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Selinexor (drug)]] 5 µM 0.312× (z -11.9) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 157 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.9) ⚠ cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 5 µM 0.476× (z -11.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H460 (line)]] | wt | 61.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Selinexor (drug)]] 5 µM 0.483× (z -9.3) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Panc 03.27 (line)]] | alt | 77.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[RPMI-7951 (line)]] | alt | 86.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.0) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[HEC-1-A (line)]] | alt | 123 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.8) |
| [[Hs 766T (line)]] | wt | 52.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 57.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 100 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.90× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H23 (line)]] | alt | 132 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -11.4) |
| [[RKO (line)]] | wt | 146 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.8) |
| [[SW1417 (line)]] | alt | 78.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[C-33 A (line)]] | alt | 158 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.5) ⚠ cell-cycle shift, explains ~66% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -10.9) |
| [[HT-29 (line)]] | alt | 42.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[KATO III (line)]] | alt | 56.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H1573 (line)]] | alt | 25.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H2347 (line)]] | alt | 83.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +14.6) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Selinexor (drug)]] 5 µM 0.450× (z -10.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[CHP-212 (line)]] | wt | 56.9 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0764× (z -11.0) |
| [[COLO 205 (line)]] | alt | 48.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[HCT15 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.480× (z -8.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HepG2_C3A (line)]] | wt | 46.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.9) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SW48 (line)]] | wt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[AN3 CA (line)]] | alt | 123 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC1A]] | +0.82 | +0.76 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 496 |
| [[HELLS]] | +0.78 | +0.79 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 703 |
| [[SKA3]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[MCM2]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 410 |
| [[XRCC2]] | +0.76 | +0.70 / +0.82 | both halves | 7e-06 |  |
| [[MCM4]] | +0.76 | +0.75 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 456 |
| [[E2F8]] | +0.76 | +0.78 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[NCAPH]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[MCM3]] | +0.75 | +0.70 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 700 |
| [[NCAPG2]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[MCM10]] | +0.75 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[RRM2]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises DNMT1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without MYBL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises DNMT1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.26× lower at baseline in the lines without CDC25A | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises DNMT1's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib) | 50% of the class's compounds vs 3.9% of all compounds | 0.060 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises DNMT1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[AURKB]] | C | AURKB activity raises DNMT1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without AURKB | 0.041 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises DNMT1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.43× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises DNMT1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without MCM10 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises DNMT1's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.27× lower at baseline in the lines without PKMYT1 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises DNMT1's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 2.39× lower at baseline in the lines without DIAPH3, MELK | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CENPP]] | C | CENPP activity raises DNMT1's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without CENPP | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.8, -43.0); signed map (-35.4, -47.8). **Vector** length 132, 52.1% of its response variance represented; |z| ≥ 3 in 1,477 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.61 to 28); *DNA Replication* (reactome, mean cos +0.59 to 40); *E2F G1/S* (control, mean cos +0.60 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.4 | +12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.5 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +4.1 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +4.0 | +22.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.8 | +15.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +0.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.6 | +0.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.5 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -10.8 | -11.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | -8.5 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.6 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -0.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | DNA methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,133,342-10,231,286 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCMT, CXXC9; previously DNMT |
| Gene groups (HGNC) | Zinc fingers CXXC-type; 7BS C5-cytosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Hallmark sets | E2F_TARGETS |
| Reactome | 17 pathways, smallest: STAT3 nuclear events downstream of ALK signaling; SUMOylation of DNA methylation proteins; DNA methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P26358](https://www.uniprot.org/uniprotkb/P26358) (DNA):

> DNA methyltransferase that methylates CpG residues. Preferentially methylates hemimethylated DNA. Associates with DNA replication sites in S phase maintaining the methylation pattern in the newly synthesized strand, that is essential for epigenetic inheritance. Associates with chromatin during G2 and M phases to maintain DNA methylation independently of replication. It is responsible for maintaining methylation patterns established in development. DNA methylation is coordinated with methylation …

**Summary**, from NCBI Gene [1786](https://www.ncbi.nlm.nih.gov/gene/1786):

> This gene encodes an enzyme that transfers methyl groups to cytosine nucleotides of genomic DNA. This protein is the major enzyme responsible for maintaining methylation patterns following DNA replication and shows a preference for hemi-methylated DNA. Methylation of DNA is an important component of mammalian epigenetic gene regulation. Aberrant methylation patterns are found in human tumors and associated with developmental abnormalities. Variation in this gene has been associated with …

**Accessions** — [HGNC:2976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2976) · Entrez [1786](https://www.ncbi.nlm.nih.gov/gene/1786) · UniProt [P26358](https://www.uniprot.org/uniprotkb/P26358) · Ensembl [ENSG00000130816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130816)

## Data

Gene col 5133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5133); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5133]; `tensor/DDL_lfc|DDL_z.npy` [5133]; `embed/gene_vectors.npy` [5133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5133 or target_col == 5133). Every well: [[DNMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
