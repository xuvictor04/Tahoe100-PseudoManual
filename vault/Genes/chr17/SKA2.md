---
symbol: "SKA2"
type: "gene"
col: 11309
ensembl_id: "ENSG00000182628"
name: "spindle and kinetochore associated complex subunit 2"
location: "17q23.2"
module: 22
arm: "+"
pooled_cpm: 46.81
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SKA2

*spindle and kinetochore associated complex subunit 2* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (23 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.48× (z +23.3, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +15.5, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.579× (z -9.9, q 3e-20, down in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.645× (z -7.9, q 4e-13, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUSAP1]] (+0.76, fdr 7e-06), [[STMN1]] (+0.76, fdr 7e-06), [[NCAPD2]] (+0.75, fdr 7e-06); moves opposite to [[ZNF761]] (-0.62, fdr 1e-05), [[ZFAND2A]] (-0.61, fdr 2e-05), [[ZNF581]] (-0.59, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 27 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.48×** | +23.3 | 0e+00 | 44/48 (NCI-H460, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.99×** | +19.9 | 0e+00 | 43/46 (Panc 03.27, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.75×** | +18.3 | 0e+00 | 47/47 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.57×** | +16.4 | 0e+00 | 38/39 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.47×** | +16.4 | 0e+00 | 46/48 (BT-474, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +15.5 | 0e+00 | 44/48 (Panc 03.27, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.21×** | +13.3 | 3e-38 | 40/45 (CFPAC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.99×** | +12.5 | 1e-33 | 42/47 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.95×** | +12.1 | 4e-32 | 43/48 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.86×** | +10.8 | 2e-25 | 40/48 (LOX-IMVI, J82, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.77×** | +10.3 | 2e-23 | 41/48 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.66×** | +8.9 | 3e-17 | 37/47 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.61×** | +8.7 | 2e-16 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.53×** | +7.7 | 4e-13 | 30/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.52×** | +7.6 | 1e-12 | 35/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.4 | 2e-06 | 24/48 (Hs 766T, HOP62, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +4.4 | 3e-04 | 16/48 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.037 | 11/47 (hTERT-HPNE, HT-29, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.051 | 9/48 (A549, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11309.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.579×** | -9.9 | 3e-20 | 42/48 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.577×** | -9.4 | 2e-18 | 35/48 (SW1417, A-427, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.645×** | -7.9 | 4e-13 | 32/47 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.735×** | -5.6 | 4e-06 | 24/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.729×** | -5.5 | 4e-06 | 27/47 (NCI-H2030, HOP62, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.583×** | -4.3 | 0.002 | 21/47 (BT-474, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.799×** | -4.1 | 0.004 | 17/48 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **0.607×** | -4.0 | 0.005 | 18/43 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.815×** | -3.7 | 0.014 | 22/48 (RKO, HCT15, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.813×** | -3.5 | 0.024 | 15/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.649×** | -3.4 | 0.032 | 15/46 (H4, A498, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.831×** | -3.3 | 0.038 | 14/47 (A498, HOP62, …) | top dose only |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.772×** | -3.3 | 0.038 | 9/48 (SW480, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.827×** | -3.3 | 0.040 | 10/48 (C-33 A, SW480, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.054 | 11/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.839× | -3.2 | 0.056 | 18/48 (SHP-77, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.6 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 190 | 5 (5 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +14.3) ⚠ cell-cycle shift, explains ~46% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.385× (z -10.4) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 51.6 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.2) | — |
| [[KATO III (line)]] | alt | 45.4 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.81× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 62.5 | 7 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +11.9) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[A549 (line)]] | wt | 46.2 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +17.6) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[LOX-IMVI (line)]] | wt | 44.7 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +15.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.6) ⚠ cell-cycle shift, explains ~49% of this change | [[AZD2858 (drug)]] 0.5 µM 0.127× (z -10.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 92.0 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Bortezomib (drug)]] 0.05 µM 0.374× (z -9.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HEC-1-A (line)]] | alt | 117 | 3 (3 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.02× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.438× (z -10.7) |
| [[HOP62 (line)]] | alt | 56.5 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.4) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[J82 (line)]] | alt | 65.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +17.9) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 44.8 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +17.5) ⚠ cell-cycle shift, explains ~49% of this change | [[Bortezomib (drug)]] 5 µM 0.0448× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[RKO (line)]] | wt | 49.2 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +13.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SW1417 (line)]] | alt | 52.5 | 3 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.7) | [[Bortezomib (drug)]] 0.05 µM 0.330× (z -10.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 49.6 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.369× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 18.8 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.11× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 37.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +18.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[Panc 03.27 (line)]] | alt | 49.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 36.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 57.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.4) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[H4 (line)]] | wt | 40.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 5.03× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.294× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 25.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HT-29 (line)]] | alt | 29.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[LS 180 (line)]] | wt | 21.7 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.59× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-1 (line)]] | wt | 54.1 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +11.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2347 (line)]] | alt | 54.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 51.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.3) | [[Auranofin (drug)]] 5 µM 0.262× (z -11.4) |
| [[SW 900 (line)]] | alt | 55.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A498 (line)]] | wt | 57.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HCT15 (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +8.9) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H2030 (line)]] | alt | 48.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[RPMI-7951 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +10.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[SW48 (line)]] | wt | 25.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUSAP1]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[STMN1]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[NCAPD2]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[H2AZ2]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[NCAPG]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[NDC80]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 890 |
| [[CDK1]] | +0.73 | +0.74 / +0.72 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 581 |
| [[ECT2]] | +0.72 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[KIF11]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TPX2]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[BIRC5]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| [[SCLT1]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF761]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[ZFAND2A]] | -0.61 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[ZNF581]] | -0.59 | -0.53 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SKA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AURKB]] | C | AURKB activity raises SKA2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without AURKB | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises SKA2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without PBK | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises SKA2's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 2.40× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises SKA2's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.06× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.8, -53.8); signed map (-47.9, -44.9). **Vector** length 117, 38.6% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.55 to 60); *DREAM G2/M down* (control, mean cos +0.58 to 28); *E2F targets* (hallmark, mean cos +0.55 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.5 | +18.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.4 | +16.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.8 | +12.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.2 | +12.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.8 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.1 | +0.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -11.2 | -9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -10.3 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.9 | -9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.9 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.1 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.5 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -5.4 | -4.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | spindle and kinetochore associated complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:59,109,857-59,155,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12758; previously FAM33A |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVK7](https://www.uniprot.org/uniprotkb/Q8WVK7) (Spindle and kinetochore-associated protein 2):

> Component of the SKA1 complex, a microtubule-binding subcomplex of the outer kinetochore that is essential for proper chromosome segregation. Required for timely anaphase onset during mitosis, when chromosomes undergo bipolar attachment on spindle microtubules leading to silencing of the spindle checkpoint. The SKA1 complex is a direct component of the kinetochore-microtubule interface and directly associates with microtubules as oligomeric assemblies. The complex facilitates the processive …

**Summary**, from NCBI Gene [348235](https://www.ncbi.nlm.nih.gov/gene/348235):

> Enables microtubule binding activity. Involved in attachment of mitotic spindle microtubules to kinetochore and regulation of microtubule polymerization or depolymerization. Located in kinetochore and spindle microtubule. Part of SKA complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28006) · Entrez [348235](https://www.ncbi.nlm.nih.gov/gene/348235) · UniProt [Q8WVK7](https://www.uniprot.org/uniprotkb/Q8WVK7) · Ensembl [ENSG00000182628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182628)

## Data

Gene col 11309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11309); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11309]; `tensor/DDL_lfc|DDL_z.npy` [11309]; `embed/gene_vectors.npy` [11309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11309 or target_col == 11309). Every well: [[SKA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
