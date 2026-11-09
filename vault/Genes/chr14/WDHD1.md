---
symbol: "WDHD1"
type: "gene"
col: 12616
ensembl_id: "ENSG00000198554"
name: "WD repeat and HMG-box DNA binding protein 1"
location: "14q22.2-q22.3"
module: 6
arm: "+"
pooled_cpm: 42.95
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 19
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# WDHD1

*WD repeat and HMG-box DNA binding protein 1* — 14q22.2-q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (26 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.43× (z +17.6, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~84% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.30× (z +7.3, q 3e-11, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.756× (z -7.9, q 2e-12, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.749× (z -5.8, q 2e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLQ]] (+0.92, fdr 7e-06), [[GINS1]] (+0.92, fdr 7e-06), [[EXO1]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 31 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 26 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **2.43×** | +17.6 | 0e+00 | 43/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **2.39×** | +17.2 | 0e+00 | 43/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **2.25×** | +16.0 | 0e+00 | 45/48 (A549, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.56×** | +8.8 | 2e-16 | 27/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.33×** | +7.9 | 4e-13 | 22/47 (AsPC-1, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.45×** | +7.4 | 2e-11 | 29/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.3 | 3e-11 | 21/48 (SW1417, SW480, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.28×** | +7.0 | 3e-10 | 26/48 (A-427, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +6.1 | 7e-08 | 26/47 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +5.6 | 9e-07 | 18/40 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +5.6 | 1e-06 | 24/48 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +5.6 | 1e-06 | 22/48 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.33×** | +5.6 | 1e-06 | 20/48 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.32×** | +5.5 | 1e-06 | 19/48 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +5.5 | 1e-06 | 19/48 (NCI-H2347, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.3 | 4e-04 | 15/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 1e-03 | 15/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 1e-03 | 18/48 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.005 | 12/48 (SW480, LS 180, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.005 | 12/48 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.007 | 14/48 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.009 | 15/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.026 | 8/48 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.041 | 12/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 5 µM |  | **1.30×** | +2.7 | 0.082 | 5/48 (A-427, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.16× | +2.7 | 0.089 | 10/47 (A-427, RKO, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.756×** | -7.9 | 2e-12 | 27/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.689×** | -7.4 | 4e-11 | 28/48 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.749×** | -5.8 | 2e-06 | 25/48 (C-33 A, SHP-77, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.683×** | -5.4 | 9e-06 | 25/48 (KATO III, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.752×** | -4.9 | 1e-04 | 16/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.843× | -4.8 | 1e-04 | 15/48 (COLO 205, SNU-1, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.629×** | -4.8 | 1e-04 | 17/47 (SW480, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.845× | -4.7 | 1e-04 | 15/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.760×** | -4.7 | 1e-04 | 25/48 (A-427, SW48, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.796×** | -4.5 | 3e-04 | 19/48 (HCT15, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.854× | -4.5 | 4e-04 | 18/48 (HCT15, SW 1088, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.800×** | -4.5 | 4e-04 | 18/48 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.753×** | -4.0 | 0.002 | 17/48 (HOP62, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.824×** | -3.9 | 0.004 | 16/48 (hTERT-HPNE, SW480, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.827×** | -3.8 | 0.006 | 17/47 (NCI-H23, HOP62, …) | two highest doses | low cells (technical?) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.838× | -3.5 | 0.012 | 14/48 (NCI-H23, SW 1271, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.712×** | -3.5 | 0.012 | 11/48 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.715×** | -3.5 | 0.013 | 11/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.024 | 18/47 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.892× | -3.2 | 0.029 | 14/48 (HOP62, SHP-77, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.036 | 11/47 (A-427, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.849× | -3.1 | 0.036 | 13/47 (A-427, HOP62, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.740×** | -3.1 | 0.036 | 12/47 (A-427, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.14 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 89.0 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.281× (z -18.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A498 (line)]] | wt | 33.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +10.5) ⚠ cell-cycle shift, explains ~84% of this change | [[Selinexor (drug)]] 5 µM 0.463× (z -10.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[MIA PaCa-2 (line)]] | alt | 53.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.263× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 38.1 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +10.2) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[A549 (line)]] | wt | 27.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +10.2) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.298× (z -12.1) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -9.2) |
| [[AN3 CA (line)]] | alt | 79.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Oxaprozin (drug)]] 0.5 µM 0.207× (z -8.8) |
| [[J82 (line)]] | alt | 82.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.386× (z -12.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 25.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +9.5) ⚠ cell-cycle shift, explains ~84% of this change | [[Selinexor (drug)]] 5 µM 0.412× (z -9.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[PANC-1 (line)]] | alt | 39.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +10.0) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[SW48 (line)]] | wt | 73.1 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.198× (z -9.6) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.377× (z -9.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[AsPC-1 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +10.9) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[C32 (line)]] | wt | 32.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.0) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.42× (z +8.5) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[COLO 205 (line)]] | alt | 23.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.285× (z -8.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HCT15 (line)]] | alt | 51.9 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.208× (z -9.4) ⚠ cell-cycle shift, explains ~87% of this change |
| [[HEC-1-A (line)]] | alt | 68.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.350× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.282× (z -11.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H1573 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +8.5) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.81× (z +9.0) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 64.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 108 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.442× (z -8.9) |
| [[SNU-423 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.4) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[BT-474 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLQ]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | STRING 479 |
| [[GINS1]] | +0.92 | +0.89 / +0.94 | both halves | 7e-06 | STRING 996 |
| [[EXO1]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | STRING 935 |
| [[BLM]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | STRING 631 |
| [[MELK]] | +0.90 | +0.86 / +0.91 | both halves | 7e-06 | STRING 569 |
| [[DTL]] | +0.90 | +0.86 / +0.92 | both halves | 7e-06 | same gene group; STRING 947 |
| [[FANCI]] | +0.90 | +0.87 / +0.88 | both halves | 7e-06 | STRING 519 |
| [[CENPK]] | +0.90 | +0.87 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[BRIP1]] | +0.89 | +0.86 / +0.91 | both halves | 7e-06 | STRING 717 |
| [[ATAD5]] | +0.88 | +0.85 / +0.91 | both halves | 7e-06 | STRING 955 |
| [[CDC45]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | STRING 999 |
| [[ATAD2]] | +0.88 | +0.82 / +0.91 | both halves | 7e-06 | STRING 445 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 8, C 11. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises WDHD1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.52× lower at baseline in the lines without E2F8 | 0.019 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises WDHD1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.33× lower at baseline in the lines without TCF19 | 0.024 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises WDHD1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.12× lower at baseline in the lines without CDC25A | 0.031 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers WDHD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF66]] | B | ZNF66 activity raises WDHD1's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without ZNF66 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[E2F2]] | B | E2F2 activity raises WDHD1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without E2F2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises WDHD1's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.14× lower at baseline in the lines without CDCA7 | 0.045 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers WDHD1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises WDHD1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.43× lower at baseline in the lines without DSCC1 | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MCM10]] | C | MCM10's natural level weakens WDHD1's drug response | MCM10's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.05; direction not clear | 0.042 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PBK]] | C | PBK activity raises WDHD1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without PBK | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises WDHD1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.68× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.937). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.0, -46.2); signed map (-39.2, -44.2). **Vector** length 137, 44.6% of its response variance represented; |z| ≥ 3 in 1,364 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.70 to 65); *DNA strand elongation* (reactome, mean cos +0.75 to 28); *DNA Replication* (reactome, mean cos +0.74 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +5.2 | +7.4 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.5 | +7.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.3 | +5.6 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +4.2 | +4.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +5.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.3 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +4.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.8 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -7.1 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -5.6 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.6 | -4.7 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat and HMG-box DNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.2-q22.3 — chr14:54,938,949-55,027,105 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AND-1, CTF4, CHTF4 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75717](https://www.uniprot.org/uniprotkb/O75717) (WD repeat and HMG-box DNA-binding protein 1):

> Core replisome component that acts as a replication initiation factor. Binds directly to the CMG complex and functions as a hub to recruit additional proteins to the replication fork.

**Summary**, from NCBI Gene [11169](https://www.ncbi.nlm.nih.gov/gene/11169):

> The protein encoded by this gene contains multiple N-terminal WD40 domains and a C-terminal high mobility group (HMG) box. WD40 domains are found in a variety of eukaryotic proteins and may function as adaptor/regulatory modules in signal transduction, pre-mRNA processing and cytoskeleton assembly. HMG boxes are found in many eukaryotic proteins involved in chromatin assembly, transcription and replication. Alternative splicing results in two transcript variants encoding different isoforms. …

**Accessions** — [HGNC:23170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23170) · Entrez [11169](https://www.ncbi.nlm.nih.gov/gene/11169) · UniProt [O75717](https://www.uniprot.org/uniprotkb/O75717) · Ensembl [ENSG00000198554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198554)

## Data

Gene col 12616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12616); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12616]; `tensor/DDL_lfc|DDL_z.npy` [12616]; `embed/gene_vectors.npy` [12616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12616 or target_col == 12616). Every well: [[WDHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
