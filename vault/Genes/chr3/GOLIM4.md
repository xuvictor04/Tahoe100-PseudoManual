---
symbol: "GOLIM4"
type: "gene"
col: 10441
ensembl_id: "ENSG00000173905"
name: "golgi integral membrane protein 4"
location: "3q26.2"
module: 114
arm: "+"
pooled_cpm: 107.88
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# GOLIM4

*golgi integral membrane protein 4* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.93× (z +16.8, q 0e+00, up in 39 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.70× (z +13.5, q 2e-39, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.636× (z -11.5, q 1e-27, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.677× (z -9.9, q 1e-20, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPSS1]] (+0.55, fdr 3e-05), [[TTC3]] (+0.54, fdr 4e-05), [[DNAJC10]] (+0.54, fdr 3e-05); moves opposite to [[TEFM]] (-0.59, fdr 1e-05), [[ZNF701]] (-0.57, fdr 2e-05), [[SLC7A6OS]] (-0.56, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.93×** | +16.8 | 0e+00 | 39/49 (NCI-H1792, LoVo, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +13.5 | 2e-39 | 43/48 (KATO III, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.65×** | +12.8 | 6e-35 | 38/48 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.69×** | +12.4 | 3e-33 | 38/45 (HOP62, SW1417, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +12.2 | 3e-32 | 37/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.49×** | +10.1 | 5e-22 | 33/48 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.50×** | +9.9 | 2e-21 | 30/43 (Panc 03.27, SNU-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.41×** | +8.8 | 1e-16 | 34/48 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.41×** | +8.4 | 4e-15 | 34/47 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +7.9 | 2e-13 | 38/49 (KATO III, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +7.6 | 2e-12 | 34/48 (RKO, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +5.7 | 5e-07 | 26/49 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.25×** | +5.4 | 3e-06 | 20/50 (A-427, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.14× | +4.6 | 1e-04 | 22/49 (NCI-H460, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 1.18× | +4.0 | 0.002 | 18/48 (A-172, NCI-H460, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.030 | 8/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.10× | +3.3 | 0.030 | 3/49 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.031 | 7/48 (KATO III, C32, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.14× | +3.2 | 0.044 | 18/48 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Oxaliplatin (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.044 | 10/48 (SW480, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.083 | 9/48 (MIA PaCa-2, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.086 | 9/48 (C32, LS 180, …) | rises with dose |  |
| [[Minodronic acid (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.091 | 2/48 (SW480, A498) | top dose only | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | 1.12× | +2.8 | 0.099 | 3/48 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -11.5 | 1e-27 | 37/48 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.677×** | -9.9 | 1e-20 | 28/48 (HS-578T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -9.8 | 2e-20 | 36/48 (SW480, KATO III, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.688×** | -9.5 | 3e-19 | 41/48 (HS-578T, SNU-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.700×** | -9.1 | 1e-17 | 36/48 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -9.1 | 1e-17 | 35/48 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.791×** | -8.4 | 4e-15 | 26/48 (SW480, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.724×** | -7.7 | 7e-13 | 28/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.808×** | -7.6 | 2e-12 | 26/48 (HS-578T, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.762×** | -6.9 | 3e-10 | 31/48 (SW480, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.763×** | -6.8 | 4e-10 | 26/48 (H4, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -6.8 | 4e-10 | 28/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.767×** | -6.7 | 8e-10 | 23/48 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.774×** | -6.5 | 3e-09 | 29/48 (HS-578T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.784×** | -5.7 | 4e-07 | 24/47 (HS-578T, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | 0.837× | -4.5 | 2e-04 | 18/48 (SNU-1, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.833×** | -4.4 | 4e-04 | 18/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.842× | -4.3 | 4e-04 | 20/48 (C-33 A, COLO 205, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.749×** | -3.8 | 0.004 | 18/49 (A-427, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 90.5 | 5 (2 ⚠) | 8 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.06× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.135× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.376× (z -11.8) |
| [[HS-578T (line)]] | alt | 231 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -18.3) |
| [[SW480 (line)]] | alt | 152 | 0 | 9 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.389× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 44.3 | 6 (5 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.35× (z +13.4) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.19× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.478× (z -9.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 149 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.341× (z -11.4) |
| [[LoVo (line)]] | wt | 62.9 | 2 (1 ⚠) | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.09× (z +11.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.384× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 54.0 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 46.4 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.09× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 151 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.484× (z -11.1) |
| [[SNU-1 (line)]] | wt | 89.4 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.54× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.253× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 30.8 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +10.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.40× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 90.7 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +10.0) | [[Selinexor (drug)]] 5 µM 0.553× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.488× (z -8.7) |
| [[SHP-77 (line)]] | alt | 214 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -10.7) |
| [[C32 (line)]] | wt | 85.9 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.8) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[H4 (line)]] | wt | 180 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0797× (z -13.4) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.430× (z -8.5) |
| [[HOP62 (line)]] | alt | 109 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.22× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Harringtonine (drug)]] 0.5 µM 0.346× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 109 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 124 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.3) | — |
| [[A498 (line)]] | wt | 203 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.542× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.589× (z -9.1) |
| [[J82 (line)]] | alt | 145 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.506× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 74.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2030 (line)]] | alt | 87.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.550× (z -10.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.448× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 68.1 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.64× (z +8.9) | [[Homoharringtonine (drug)]] 0.05 µM 0.482× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 73.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +16.6) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[RKO (line)]] | wt | 62.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.2) ⚠ cell-cycle shift, explains ~62% of this change | [[Digitoxin (drug)]] 5 µM 0.248× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[BT-474 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.381× (z -9.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 78.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 190 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.464× (z -8.8) |
| [[SNU-423 (line)]] | alt | 80.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.4) | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.217× (z -9.1) |
| [[A-172 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 124 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 90.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*27 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPSS1]] | +0.55 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[TTC3]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[DNAJC10]] | +0.54 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[SEC63]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[STT3B]] | +0.49 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[SETD3]] | +0.49 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[CALU]] | +0.49 | +0.40 / +0.39 | both halves | 6e-05 |  |
| [[PARP1]] | +0.48 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[CYB5A]] | +0.48 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[SSX2IP]] | +0.48 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[SSR1]] | +0.48 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[NIN]] | +0.48 | +0.39 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*73 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEFM]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ZNF701]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SLC7A6OS]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ZC3HC1]] | -0.56 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SLC25A17]] | -0.55 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[TMEM199]] | -0.55 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ZNF431]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[IGHMBP2]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GPN2]] | -0.53 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MAPK1IP1L]] | -0.53 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ZFYVE26]] | -0.52 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[SMG8]] | -0.52 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction -0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.4, 9.4); signed map (-59.2, 8.3). **Vector** length 124, 37.1% of its response variance represented; |z| ≥ 3 in 1,495 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.1 | +13.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +6.8 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +6.6 | +8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +0.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.5 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -10.6 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.8 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.6 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | golgi integral membrane protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:168,008,689-168,095,924 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPP130, GIMPC, P138; previously GOLPH4 |
| Reactome | 4 pathways, smallest: Intra-Golgi traffic; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O00461](https://www.uniprot.org/uniprotkb/O00461) (Golgi integral membrane protein 4):

> Plays a role in endosome to Golgi protein trafficking; mediates protein transport along the late endosome-bypass pathway from the early endosome to the Golgi.

**Summary**, from NCBI Gene [27333](https://www.ncbi.nlm.nih.gov/gene/27333):

> The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is a type II Golgi-resident protein. It may process proteins synthesized in the rough endoplasmic reticulum and assist in the transport of protein cargo through the Golgi apparatus. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15448) · Entrez [27333](https://www.ncbi.nlm.nih.gov/gene/27333) · UniProt [O00461](https://www.uniprot.org/uniprotkb/O00461) · Ensembl [ENSG00000173905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173905)

## Data

Gene col 10441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10441); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10441]; `tensor/DDL_lfc|DDL_z.npy` [10441]; `embed/gene_vectors.npy` [10441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10441 or target_col == 10441). Every well: [[GOLIM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLIM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
