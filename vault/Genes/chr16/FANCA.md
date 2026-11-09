---
symbol: "FANCA"
type: "gene"
col: 11942
ensembl_id: "ENSG00000187741"
name: "FA complementation group A"
location: "16q24.3"
module: 6
arm: "+"
pooled_cpm: 34.6
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 32
n_dd_up_clean: 12
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FANCA

*FA complementation group A* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (27 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.99× (z +16.2, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~77% of this change. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 1.61× (z +3.7, q 0.005, up in 15 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -13.1, q 3e-36, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC45]] (+0.93, fdr 7e-06), [[POLE]] (+0.91, fdr 7e-06), [[WDR76]] (+0.91, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 28 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 27 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **2.99×** | +16.2 | 0e+00 | 45/48 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **2.69×** | +14.7 | 0e+00 | 44/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **2.44×** | +13.2 | 1e-37 | 42/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.81×** | +8.8 | 2e-16 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.68×** | +7.7 | 2e-12 | 35/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +7.6 | 2e-12 | 31/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.60×** | +7.0 | 2e-10 | 31/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.59×** | +6.9 | 4e-10 | 32/48 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.57×** | +6.7 | 1e-09 | 28/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.57×** | +6.4 | 7e-09 | 31/47 (SNU-423, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.51×** | +6.1 | 6e-08 | 27/47 (A549, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.49×** | +5.9 | 1e-07 | 26/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.47×** | +5.5 | 2e-06 | 23/36 (LoVo, SW 900, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.49×** | +5.5 | 2e-06 | 20/42 (SW 900, Panc 03.27, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +5.4 | 2e-06 | 22/47 (A549, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.005 | 15/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.018 | 15/46 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.022 | 14/48 (NCI-H1573, C32, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.035 | 7/48 (SW480, A-427, …) | top dose only | plate-row cell shift |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.036 | 8/47 (C-33 A, J82, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.038 | 10/48 (A549, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.042 | 9/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.065 | 7/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.16× | +2.8 | 0.080 | 8/48 (J82, SW480, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.21×** | +2.8 | 0.089 | 10/45 (RPMI-7951, BT-474, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +2.7 | 0.089 | 11/46 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.20×** | +2.7 | 0.096 | 6/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Oxaliplatin (drug)]] 0.5 µM |  | **1.29×** | +2.7 | 0.097 | 5/48 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -13.1 | 3e-36 | 36/48 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.593×** | -10.9 | 4e-25 | 36/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.499×** | -10.3 | 1e-22 | 37/47 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.513×** | -9.9 | 5e-21 | 31/47 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.705×** | -7.3 | 4e-11 | 34/48 (KATO III, HCT15, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.572×** | -5.9 | 3e-07 | 28/48 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.664×** | -5.8 | 4e-07 | 26/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.700×** | -5.3 | 8e-06 | 25/47 (SK-MEL-2, A-172, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.747×** | -4.9 | 5e-05 | 26/48 (A-427, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.705×** | -4.7 | 1e-04 | 20/47 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.811×** | -4.4 | 6e-04 | 19/48 (HCT15, A-172, …) | two highest doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.572×** | -4.3 | 7e-04 | 21/46 (NCI-H23, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.750×** | -4.3 | 7e-04 | 21/48 (A-427, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.749×** | -4.3 | 7e-04 | 18/48 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.750×** | -4.3 | 7e-04 | 15/48 (LOX-IMVI, KATO III, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.752×** | -4.1 | 0.002 | 19/47 (A-427, HOP62, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.764×** | -4.0 | 0.002 | 19/48 (RKO, C32, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.766×** | -3.8 | 0.004 | 18/46 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.004 | 18/48 (A-427, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.780×** | -3.7 | 0.006 | 17/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.781×** | -3.7 | 0.006 | 14/47 (RKO, A-172, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.796×** | -3.4 | 0.017 | 13/47 (SK-MEL-2, RKO, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.33 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.7 | 6 (6 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.87× (z +9.7) ⚠ cell-cycle shift, explains ~77% of this change | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.1) |
| [[A-172 (line)]] | wt | 42.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.277× (z -11.5) |
| [[A-427 (line)]] | wt | 72.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -24.5) |
| [[A549 (line)]] | wt | 15.6 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.55× (z +10.6) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[HEC-1-A (line)]] | alt | 59.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -20.2) |
| [[SW48 (line)]] | wt | 46.8 | 0 | 4 (3 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.202× (z -12.2) |
| [[A498 (line)]] | wt | 61.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -15.2) |
| [[H4 (line)]] | wt | 31.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 19.8 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.34× (z +9.7) ⚠ cell-cycle shift, explains ~77% of this change | [[Selinexor (drug)]] 5 µM 0.273× (z -10.6) |
| [[LS 180 (line)]] | wt | 24.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 49.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 3.35× (z +8.5) ⚠ cell-cycle shift, explains ~97% of this change | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.7) |
| [[HOP62 (line)]] | alt | 43.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.6) |
| [[HT-29 (line)]] | alt | 20.7 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.40× (z +8.7) ⚠ cell-cycle shift, explains ~77% of this change | [[Selinexor (drug)]] 5 µM 0.298× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 14.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.97× (z +10.9) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H1792 (line)]] | alt | 9.88 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.65× (z +10.1) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H23 (line)]] | alt | 59.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 28.6 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.64× (z +9.1) ⚠ cell-cycle shift, explains ~77% of this change | [[Selinexor (drug)]] 5 µM 0.390× (z -9.4) |
| [[PANC-1 (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.89× (z +9.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.204× (z -9.6) |
| [[SNU-1 (line)]] | wt | 31.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.9) |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.8) |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.278× (z -8.6) |
| [[LoVo (line)]] | wt | 25.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +8.9) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[RKO (line)]] | wt | 57.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.266× (z -9.0) |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC45]] | +0.93 | +0.93 / +0.91 | both halves | 7e-06 | STRING 539 |
| [[POLE]] | +0.91 | +0.91 / +0.91 | both halves | 7e-06 | STRING 567 |
| [[WDR76]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[RAD54L]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | STRING 749 |
| [[EXO1]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | STRING 667 |
| [[CENPK]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[RAD51]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | same gene group; STRING 936 |
| [[DTL]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[MELK]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[BLM]] | +0.87 | +0.89 / +0.85 | both halves | 7e-06 | STRING 999 |
| [[GINS2]] | +0.87 | +0.88 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises FANCA's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without E2F2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises FANCA's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without TLCD3B | 0.025 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises FANCA's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without E2F8 | 0.033 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises FANCA's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.51× lower at baseline in the lines without CDC25A | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers FANCA's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MIR924HG]] | B | MIR924HG activity lowers FANCA's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.25× higher at baseline in the lines without MIR924HG | 0.087 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |
| [[SHMT1]] | C | SHMT1 activity raises FANCA's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[DSCC1]] | C | DSCC1 activity raises FANCA's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without DSCC1 | 0.073 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.919). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.2, -44.9); signed map (-37.6, -44.2). **Vector** length 154, 53.9% of its response variance represented; |z| ≥ 3 in 1,513 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.68 to 65); *DNA strand elongation* (reactome, mean cos +0.74 to 28); *DNA Replication* (reactome, mean cos +0.74 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.0 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.8 | +16.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.5 | +7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +5.4 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.4 | +14.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +1.2 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.6 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -11.1 | -9.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -11.0 | -10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.7 | -13.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -8.6 | -10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -4.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.1 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,726,683-89,816,977 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAA, FA-H, FAH; previously FACA, FANCH |
| Gene groups (HGNC) | FA complementation groups; FA core complex |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15360](https://www.uniprot.org/uniprotkb/O15360) (Fanconi anemia group A protein):

> DNA repair protein that may operate in a postreplication repair or a cell cycle checkpoint function. May be involved in interstrand DNA cross-link repair and in the maintenance of normal chromosome stability.

**Summary**, from NCBI Gene [2175](https://www.ncbi.nlm.nih.gov/gene/2175):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The …

**Accessions** — [HGNC:3582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3582) · Entrez [2175](https://www.ncbi.nlm.nih.gov/gene/2175) · UniProt [O15360](https://www.uniprot.org/uniprotkb/O15360) · Ensembl [ENSG00000187741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187741)

## Data

Gene col 11942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11942); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11942]; `tensor/DDL_lfc|DDL_z.npy` [11942]; `embed/gene_vectors.npy` [11942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11942 or target_col == 11942). Every well: [[FANCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
