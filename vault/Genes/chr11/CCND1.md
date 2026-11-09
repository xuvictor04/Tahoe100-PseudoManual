---
symbol: "CCND1"
type: "gene"
col: 3115
ensembl_id: "ENSG00000110092"
name: "cyclin D1"
location: "11q13.3"
module: 92
arm: "+"
pooled_cpm: 229.71
n_lines_expressing: 43
n_dd_up: 30
n_dd_down: 43
n_dd_up_clean: 12
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 6
direction_downstream: 15
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# CCND1

*cyclin D1* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.37× (z +23.8, q 0e+00, up in 42 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.75× (z +8.0, q 2e-13, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.290× (z -17.4, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYEOV]] (+0.70, fdr 7e-06), [[AGO2]] (+0.69, fdr 7e-06), [[FOSL1]] (+0.65, fdr 7e-06); moves opposite to [[EMC2]] (-0.62, fdr 1e-05), [[TENT2]] (-0.60, fdr 2e-05), [[NPEPPS]] (-0.59, fdr 1e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[UBASH3B]] → it (grade B ⚠); 15 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.37×** | +23.8 | 0e+00 | 42/42 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.83×** | +21.5 | 0e+00 | 37/38 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.71×** | +17.2 | 0e+00 | 38/39 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +8.0 | 2e-13 | 33/41 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.67×** | +7.0 | 2e-10 | 28/40 (C32, SW1417, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.67×** | +7.0 | 2e-10 | 28/41 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +6.9 | 3e-10 | 26/40 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.57×** | +6.4 | 9e-09 | 28/41 (HS-578T, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.54×** | +6.1 | 5e-08 | 25/41 (HS-578T, SNU-423, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +5.8 | 3e-07 | 23/41 (SNU-423, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.48×** | +5.6 | 9e-07 | 22/41 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +5.6 | 1e-06 | 27/41 (C32, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.45×** | +5.3 | 6e-06 | 20/41 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.39×** | +4.7 | 1e-04 | 23/41 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.78×** | +4.3 | 7e-04 | 31/40 (NCI-H23, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +4.2 | 8e-04 | 23/41 (SW 900, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.008 | 19/40 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.009 | 20/41 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.012 | 20/41 (SK-MEL-2, J82, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.026 | 15/39 (HOP62, SW 900, …) | two highest doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.044 | 15/41 (NCI-H1573, H4, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.081 | 15/42 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.086 | 15/41 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.087 | 7/41 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.45×** | +2.8 | 0.100 | 10/42 (SNU-423, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.290×** | -17.4 | 0e+00 | 41/41 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.311×** | -17.1 | 0e+00 | 42/43 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.333×** | -15.5 | 0e+00 | 39/41 (SNU-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.322×** | -15.4 | 0e+00 | 38/40 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -12.6 | 3e-34 | 40/41 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.487×** | -12.2 | 3e-32 | 39/41 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.449×** | -11.4 | 5e-28 | 37/42 (SW480, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.485×** | -10.2 | 1e-22 | 36/42 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.483×** | -9.9 | 4e-21 | 39/41 (SW480, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.643×** | -8.7 | 2e-16 | 34/41 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.315×** | -8.5 | 8e-16 | 38/41 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.595×** | -8.5 | 8e-16 | 32/41 (SW480, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.331×** | -8.2 | 2e-14 | 35/43 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.342×** | -7.9 | 9e-14 | 38/39 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.583×** | -7.6 | 1e-12 | 32/40 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[BI-3406 (drug)]] 5 µM |  | **0.446×** | -5.9 | 8e-08 | 30/41 (HOP62, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 407 | 3 (3 ⚠) | 25 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.27× (z +18.2) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.167× (z -18.9) |
| [[Panc 03.27 (line)]] | alt | 183 | 3 (3 ⚠) | 16 | [[Dinaciclib (drug)]] 0.5 µM 6.60× (z +15.9) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.142× (z -16.7) |
| [[HOP62 (line)]] | alt | 610 | 2 (2 ⚠) | 15 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.111× (z -21.5) |
| [[HS-578T (line)]] | alt | 231 | 9 (9 ⚠) | 8 | [[Harringtonine (drug)]] 0.5 µM 3.61× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change | [[Cobimetinib (drug)]] 5 µM 0.179× (z -15.9) |
| [[PANC-1 (line)]] | alt | 210 | 3 (3 ⚠) | 14 | [[Harringtonine (drug)]] 5 µM 2.88× (z +10.0) ⚠ cell-cycle shift, explains ~63% of this change | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -15.4) |
| [[J82 (line)]] | alt | 283 | 5 (5 ⚠) | 11 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +12.1) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.141× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 4 (3 ⚠) | 10 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.31× (z +9.6) | [[Adagrasib (drug)]] 0.05 µM 0.588× (z -14.8) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.188× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 578 | 4 (4 ⚠) | 10 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.7) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.241× (z -11.6) |
| [[A498 (line)]] | wt | 146 | 0 | 13 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -15.0) |
| [[KATO III (line)]] | alt | 168 | 3 (3 ⚠) | 10 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +15.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.249× (z -11.7) |
| [[A-172 (line)]] | wt | 459 | 4 (4 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | [[Cobimetinib (drug)]] 5 µM 0.154× (z -16.2) |
| [[C32 (line)]] | wt | 130 | 6 (5 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 13.4× (z +18.8) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 3.64× (z +9.0) | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0416× (z -12.1) ⚠ toxic · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.304× (z -10.1) |
| [[H4 (line)]] | wt | 149 | 3 (3 ⚠) | 9 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +13.3) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.188× (z -12.4) |
| [[A-427 (line)]] | wt | 343 | 3 (3 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -22.0) |
| [[CFPAC-1 (line)]] | alt | 143 | 5 (5 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +13.0) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.270× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 322 | 3 (3 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +15.4) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.276× (z -12.5) |
| [[SW48 (line)]] | wt | 213 | 3 (3 ⚠) | 8 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +11.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 712 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -24.2) |
| [[NCI-H1573 (line)]] | alt | 238 | 2 (2 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 7.19× (z +13.1) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.134× (z -14.9) |
| [[SNU-423 (line)]] | alt | 96.6 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.17× (z +10.7) | — |
| [[A549 (line)]] | wt | 100 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +13.2) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 5 µM 0.112× (z -16.5) |
| [[Hs 766T (line)]] | wt | 91.0 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 6.49× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.55× (z +9.1) | [[Cobimetinib (drug)]] 5 µM 0.257× (z -9.3) |
| [[LoVo (line)]] | wt | 147 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +15.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.182× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 124 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 8.84× (z +18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.03× (z +9.3) | [[Trametinib (drug)]] 5 µM 0.316× (z -10.5) |
| [[SNU-1 (line)]] | wt | 526 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0931× (z -23.4) |
| [[AsPC-1 (line)]] | alt | 91.3 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +13.8) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 5 µM 0.269× (z -10.6) |
| [[BT-474 (line)]] | alt | 383 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -16.2) |
| [[LS 180 (line)]] | wt | 273 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +15.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.221× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 236 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -17.2) |
| [[LOX-IMVI (line)]] | wt | 123 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 9.16× (z +19.0) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.246× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 416 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -12.0) |
| [[HCT15 (line)]] | alt | 156 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +12.0) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.234× (z -9.5) |
| [[SW 900 (line)]] | alt | 105 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +16.8) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.244× (z -10.6) |
| [[SW1417 (line)]] | alt | 356 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +16.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 151 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 85.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +13.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 82.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +13.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -10.1) |
| [[CHP-212 (line)]] | wt | 203 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 34.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 57.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 37.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 56.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 55.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 46.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 175 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYEOV]] | +0.70 | +0.69 / +0.76 | both halves | 7e-06 | STRING 792 |
| [[AGO2]] | +0.69 | +0.76 / +0.61 | both halves | 7e-06 | pathway: Co-inhibition by PD-1; STRING 728 |
| [[FOSL1]] | +0.65 | +0.63 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 548 |
| [[LTBP2]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ME3]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DCBLD2]] | +0.64 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LINC00973]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SPRED1]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NT5E]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ENC1]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC2]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[TENT2]] | -0.60 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[NPEPPS]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[TOM1]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[CWC15]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ARNT]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PPP1R12B]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MARCHF5]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[RAB6A]] | -0.56 | -0.45 / -0.51 | both halves | 3e-05 | pathway: Pre-NOTCH Expression and Processing |
| [[ALKBH7]] | -0.55 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ALDH2]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBASH3B]] | B | UBASH3B activity raises CCND1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 1.93× lower at baseline in the lines without UBASH3B | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[LINC01844]] | B | LINC01844 activity raises CCND1's level | lines that do not express LINC01844 (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without LINC01844 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000287712, ADGRG2, ENSG00000291283; maybe low, not absent |
| [[LINC00973]] | B | LINC00973 activity raises CCND1's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without LINC00973 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |
| [[GJC1]] | B | GJC1 activity raises CCND1's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without GJC1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[MAMLD1]] | B | MAMLD1 activity raises CCND1's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without MAMLD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[ITGA6]] | B | ITGA6 activity raises CCND1's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without ITGA6 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | CCND1 activity raises EPHA2's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.30× lower at baseline in the lines without CCND1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[PPP1R12B]] | B | CCND1 activity lowers PPP1R12B's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.18× higher at baseline in the lines without CCND1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[PXN]] | B | CCND1 activity raises PXN's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.11× lower at baseline in the lines without CCND1 | 0.015 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[MAMLD1]] | B | CCND1 activity raises MAMLD1's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.42× lower at baseline in the lines without CCND1 | 0.017 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[TNFRSF12A]] | B | CCND1 activity raises TNFRSF12A's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without CCND1 | 0.026 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[ELK3]] | B | CCND1 activity raises ELK3's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.45× lower at baseline in the lines without CCND1 | 0.036 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[MYL12A]] | B | CCND1 activity raises MYL12A's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without CCND1 | 0.036 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[SARNP]] | B | CCND1 activity raises SARNP's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.14× lower at baseline in the lines without CCND1 | 0.037 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[PLEC]] | B | CCND1 activity raises PLEC's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without CCND1 | 0.055 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[FOSL1]] | B | CCND1 activity raises FOSL1's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without CCND1 | 0.072 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[RAB3GAP1]] | B | CCND1 activity raises RAB3GAP1's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.19× lower at baseline in the lines without CCND1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| cells under [[AT7519 (drug)]] 5 µM | B | CCND1 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express CCND1 (7) vs lines expressing it (41) | the lines without CCND1: 0.60× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.3, 8.7); signed map (10.3, 44.1). **Vector** length 135, 48.6% of its response variance represented; |z| ≥ 3 in 2,164 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK family signaling cascades* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.8 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.5 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +3.5 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -9.9 | -12.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -9.5 | -17.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.5 | -9.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.3 | -10.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.3 | -11.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.3 | -15.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:69,641,156-69,654,474 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U21B31; previously BCL1, D11S287E, PRAD1 |
| Gene groups (HGNC) | Cyclins |
| Hallmark sets | NOTCH_SIGNALING, ANDROGEN_RESPONSE, APOPTOSIS, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB, G2M_CHECKPOINT |
| Reactome | 49 pathways, smallest: Drug-mediated inhibition of CDK4/CDK6 activity; PTK6 Regulates Cell Cycle; RUNX3 regulates WNT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P24385](https://www.uniprot.org/uniprotkb/P24385) (G1/S-specific cyclin-D1):

> Regulatory component of the cyclin D1-CDK4 (DC) complex that phosphorylates and inhibits members of the retinoblastoma (RB) protein family including RB1 and regulates the cell-cycle during G(1)/S transition. Phosphorylation of RB1 allows dissociation of the transcription factor E2F from the RB/E2F complex and the subsequent transcription of E2F target genes which are responsible for the progression through the G(1) phase. Hypophosphorylates RB1 in early G(1) phase. Cyclin D-CDK4 complexes are …

**Summary**, from NCBI Gene [595](https://www.ncbi.nlm.nih.gov/gene/595):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance throughout the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin forms a complex with and functions as a regulatory subunit of CDK4 or CDK6, whose activity is required for cell …

**Accessions** — [HGNC:1582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1582) · Entrez [595](https://www.ncbi.nlm.nih.gov/gene/595) · UniProt [P24385](https://www.uniprot.org/uniprotkb/P24385) · Ensembl [ENSG00000110092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110092)

## Data

Gene col 3115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3115); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3115]; `tensor/DDL_lfc|DDL_z.npy` [3115]; `embed/gene_vectors.npy` [3115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3115 or target_col == 3115). Every well: [[CCND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
