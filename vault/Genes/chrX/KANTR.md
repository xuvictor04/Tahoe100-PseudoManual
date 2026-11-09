---
symbol: "KANTR"
type: "gene"
col: 13853
ensembl_id: "ENSG00000232593"
name: "KANTR integral membrane protein"
location: "Xp11.22"
module: 85
arm: "+"
pooled_cpm: 81.04
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 37
n_dd_up_clean: 10
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# KANTR

*KANTR integral membrane protein* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.64× (z +11.1, q 9e-26, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.321× (z -25.5, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP70]] (+0.70, fdr 7e-06), [[HACE1]] (+0.64, fdr 1e-05), [[GMCL1]] (+0.64, fdr 1e-05); moves opposite to [[ITPRIPL2]] (-0.65, fdr 1e-05), [[RGS20]] (-0.60, fdr 1e-05), [[GPATCH4]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RGS20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +11.1 | 9e-26 | 36/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +10.0 | 4e-21 | 35/47 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +9.7 | 9e-20 | 31/47 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +8.1 | 6e-14 | 31/47 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +5.9 | 3e-07 | 36/48 (KATO III, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.8 | 6e-07 | 27/47 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +5.6 | 2e-06 | 23/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.56×** | +5.3 | 1e-05 | 30/46 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.6 | 3e-04 | 17/47 (SW1417, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.003 | 20/46 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.19× | +3.8 | 0.006 | 11/47 (J82, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.8 | 0.006 | 19/48 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.015 | 14/47 (SW1417, SHP-77, …) | top dose only | plate-row cell shift; position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 1.11× | +3.2 | 0.047 | 5/47 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.055 | 10/47 (KATO III, A-172, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.059 | 13/47 (NCI-H460, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.321×** | -25.5 | 0e+00 | 46/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.485×** | -23.0 | 0e+00 | 43/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.347×** | -22.8 | 0e+00 | 45/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.460×** | -17.5 | 0e+00 | 44/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.468×** | -17.0 | 0e+00 | 43/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -16.7 | 0e+00 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -13.1 | 4e-37 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.560×** | -13.0 | 9e-37 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.614×** | -10.9 | 4e-26 | 40/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.416×** | -10.3 | 4e-23 | 39/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -10.1 | 4e-22 | 40/46 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -9.9 | 1e-21 | 34/43 (SNU-423, LS 180, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -9.2 | 1e-18 | 35/46 (SNU-423, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.674×** | -8.9 | 3e-17 | 34/47 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -8.8 | 4e-17 | 41/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -6.6 | 1e-09 | 27/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -6.2 | 1e-08 | 25/47 (A-427, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.780×** | -5.6 | 7e-07 | 25/47 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.780×** | -5.6 | 7e-07 | 26/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.636×** | -5.3 | 3e-06 | 28/47 (Hs 766T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 84.9 | 3 | 14 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -33.1) |
| [[NCI-H460 (line)]] | wt | 87.5 | 1 | 14 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.22× (z +9.0) | [[Harringtonine (drug)]] 0.5 µM 0.137× (z -22.3) |
| [[SW480 (line)]] | alt | 147 | 0 | 15 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.325× (z -18.2) |
| [[SNU-423 (line)]] | alt | 184 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -35.4) |
| [[NCI-H1573 (line)]] | alt | 54.8 | 4 (1 ⚠) | 9 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.07× (z +11.0) | [[Harringtonine (drug)]] 0.5 µM 0.212× (z -15.2) |
| [[C32 (line)]] | wt | 105 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -18.0) |
| [[A549 (line)]] | wt | 55.8 | 1 | 8 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -20.5) |
| [[A-427 (line)]] | wt | 96.0 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.369× (z -11.9) |
| [[Hs 766T (line)]] | wt | 105 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -13.7) |
| [[HOP62 (line)]] | alt | 127 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.195× (z -20.3) |
| [[SNU-1 (line)]] | wt | 86.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -16.7) |
| [[HCT15 (line)]] | alt | 101 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 89.0 | 1 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -13.3) |
| [[SW 900 (line)]] | alt | 59.9 | 0 | 6 | — | [[Harringtonine (drug)]] 0.5 µM 0.203× (z -14.2) |
| [[A498 (line)]] | wt | 32.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -16.5) |
| [[BT-474 (line)]] | alt | 59.5 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -13.9) |
| [[COLO 205 (line)]] | alt | 97.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -17.4) |
| [[HS-578T (line)]] | alt | 52.5 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -13.6) |
| [[HT-29 (line)]] | alt | 92.5 | 1 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -12.2) |
| [[KATO III (line)]] | alt | 79.1 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.53× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 66.3 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -18.5) |
| [[SHP-77 (line)]] | alt | 298 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -13.1) |
| [[SW1417 (line)]] | alt | 99.0 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.401× (z -11.2) ⚠ toxic |
| [[SW48 (line)]] | wt | 64.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.233× (z -10.8) |
| [[A-172 (line)]] | wt | 64.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -14.4) |
| [[H4 (line)]] | wt | 101 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -14.1) |
| [[LoVo (line)]] | wt | 59.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.283× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -10.5) |
| [[LS 180 (line)]] | wt | 65.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.396× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 54.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 61.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.272× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 49.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -20.7) |
| [[SK-MEL-2 (line)]] | alt | 81.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -12.6) |
| [[AN3 CA (line)]] | alt | 173 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0709× (z -9.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 45.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -12.8) |
| [[CHP-212 (line)]] | wt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 46.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.255× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 56.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.255× (z -10.9) |
| [[J82 (line)]] | alt | 90.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.381× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 37.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.5) |
| [[C-33 A (line)]] | alt | 76.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -9.4) |
| [[RKO (line)]] | wt | 41.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.306× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP70]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[HACE1]] | +0.64 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PDK3]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[HAUS4]] | +0.63 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SNAPC3]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.61 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[HSPB11]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PLEKHH3]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PHKA2]] | +0.61 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[KIAA1328]] | +0.61 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[FAM13B]] | +0.60 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPRIPL2]] | -0.65 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[RGS20]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.60 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[AEN]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[AVEN]] | -0.59 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[ST7L]] | -0.59 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SMCO2]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ITPA]] | -0.58 | -0.55 / -0.43 | both halves | 4e-05 |  |
| [[ANKLE2]] | -0.58 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[BMPR1B]] | -0.57 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SUSD1]] | -0.57 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.57 | -0.57 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS20]] | B | RGS20 activity lowers KANTR's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without RGS20 | 0.008 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[SYNGR1]] | B | SYNGR1 activity raises KANTR's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 1.37× lower at baseline in the lines without SYNGR1 | 0.020 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[SMCO2]] | B | SMCO2 activity lowers KANTR's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.78× higher at baseline in the lines without SMCO2 | 0.040 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers KANTR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises KANTR's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without WARS2-AS1 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.9, -9.9); signed map (-35.6, 16.3). **Vector** length 105, 33.9% of its response variance represented; |z| ≥ 3 in 1,659 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM |  | +6.0 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +11.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +0.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.4 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.0 | -25.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.0 | -17.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.3 | -10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -4.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | KANTR integral membrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:53,094,142-53,170,914 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Spasm; previously LINC01155 |
| Matched by | ensembl_id |

UniProt [A0A1W2PQU2](https://www.uniprot.org/uniprotkb/A0A1W2PQU2) carries no function annotation.

**Summary**, from NCBI Gene [102723508](https://www.ncbi.nlm.nih.gov/gene/102723508):

> This gene is thought to produce a functional long non-coding RNA. Mutation of this locus in mouse causes tremors and spastic movements, suggesting a role for this gene in neurological development or function. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:49510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49510) · Entrez [102723508](https://www.ncbi.nlm.nih.gov/gene/102723508) · UniProt [A0A1W2PQU2](https://www.uniprot.org/uniprotkb/A0A1W2PQU2) · Ensembl [ENSG00000232593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232593)

## Data

Gene col 13853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13853); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13853]; `tensor/DDL_lfc|DDL_z.npy` [13853]; `embed/gene_vectors.npy` [13853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13853 or target_col == 13853). Every well: [[KANTR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANTR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
