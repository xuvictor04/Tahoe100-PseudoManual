---
symbol: "FANCB"
type: "gene"
col: 11195
ensembl_id: "ENSG00000181544"
name: "FA complementation group B"
location: "Xp22.2"
module: 6
arm: "+"
pooled_cpm: 44.19
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FANCB

*FA complementation group B* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (26 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.57× (z +29.9, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.28× (z +6.8, q 1e-09, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.667× (z -11.3, q 6e-27, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.753× (z -5.6, q 3e-06, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLM]] (+0.93, fdr 7e-06), [[CENPK]] (+0.92, fdr 7e-06), [[EXO1]] (+0.91, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 32 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 26 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **4.57×** | +29.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **3.81×** | +26.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **3.74×** | +26.0 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.76×** | +11.1 | 1e-26 | 39/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.53×** | +8.3 | 1e-14 | 34/48 (SW480, LoVo, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.29×** | +7.1 | 1e-10 | 29/48 (RKO, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +6.8 | 1e-09 | 26/48 (SW1417, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.41×** | +6.7 | 1e-09 | 27/48 (A-427, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.41×** | +6.7 | 2e-09 | 28/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +6.6 | 2e-09 | 25/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +6.5 | 5e-09 | 22/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.39×** | +6.4 | 7e-09 | 26/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.40×** | +6.4 | 9e-09 | 25/46 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.36×** | +6.1 | 6e-08 | 27/47 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.37×** | +6.0 | 8e-08 | 24/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 2e-07 | 23/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 4e-04 | 20/48 (SW480, J82, …) | rises with dose | plate-row cell shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.002 | 15/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.004 | 17/48 (NCI-H460, H4, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.010 | 8/48 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.027 | 13/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.034 | 5/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.040 | 7/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +2.9 | 0.047 | 12/48 (SW480, J82, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.047 | 7/48 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.054 | 11/47 (C32, A-427, …) | all doses, stronger at high dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.23×** | +2.8 | 0.054 | 9/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.054 | 11/48 (BT-474, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.667×** | -11.3 | 6e-27 | 29/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.601×** | -10.1 | 2e-21 | 35/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.669×** | -5.7 | 3e-06 | 20/48 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.753×** | -5.6 | 3e-06 | 22/47 (SK-MEL-2, H4, …) | two highest doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.769×** | -5.2 | 2e-05 | 25/48 (hTERT-HPNE, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.787×** | -4.8 | 2e-04 | 17/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.848× | -4.6 | 3e-04 | 14/48 (HCT15, RKO, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.793×** | -4.4 | 7e-04 | 18/47 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.859× | -4.3 | 0.001 | 23/48 (H4, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.826×** | -4.3 | 0.001 | 18/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.807×** | -4.1 | 0.002 | 17/47 (A-427, NCI-H2030, …) | two highest doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.814×** | -4.1 | 0.002 | 14/48 (SW 1088, CFPAC-1, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.867× | -4.0 | 0.003 | 16/48 (LoVo, A-172, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.628×** | -3.9 | 0.003 | 14/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.817×** | -3.8 | 0.004 | 19/47 (A-427, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.799×** | -3.8 | 0.005 | 14/48 (A-427, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.839× | -3.5 | 0.014 | 11/47 (COLO 205, NCI-H23, …) | two highest doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.787×** | -3.4 | 0.019 | 9/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.793×** | -3.3 | 0.024 | 13/48 (SW480, RKO, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.861× | -3.0 | 0.066 | 12/48 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.716×** | -2.8 | 0.097 | 12/45 (SW480, KATO III, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.10 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.1 | 3 (3 ⚠) | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.75× (z +10.2) ⚠ cell-cycle shift, explains ~47% of this change | [[Selinexor (drug)]] 5 µM 0.234× (z -16.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.466× (z -8.5) |
| [[A-172 (line)]] | wt | 61.2 | 4 (4 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.309× (z -11.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.5 µM 0.229× (z -10.2) |
| [[A-427 (line)]] | wt | 62.0 | 3 (3 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +9.2) ⚠ cell-cycle shift, explains ~46% of this change | [[Selinexor (drug)]] 5 µM 0.224× (z -18.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 46.3 | 1 (1 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.06× (z +8.6) ⚠ cell-cycle shift, explains ~47% of this change | [[Docetaxel (drug)]] 0.05 µM 0.0727× (z -13.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.274× (z -9.7) |
| [[J82 (line)]] | alt | 117 | 3 (3 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.44× (z +11.9) ⚠ cell-cycle shift, explains ~47% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 34.3 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.66× (z +13.4) ⚠ cell-cycle shift, explains ~47% of this change | [[Selinexor (drug)]] 5 µM 0.331× (z -13.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 89.2 | 4 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.88× (z +12.5) ⚠ cell-cycle shift, explains ~47% of this change | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 44.7 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.08× (z +15.7) ⚠ cell-cycle shift, explains ~46% of this change | [[Selinexor (drug)]] 5 µM 0.478× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 78.9 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +10.1) ⚠ cell-cycle shift, explains ~47% of this change | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 21.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 91.4 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +18.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A549 (line)]] | wt | 32.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.75× (z +14.1) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[BT-474 (line)]] | alt | 55.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +11.2) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +11.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[Hs 766T (line)]] | wt | 35.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.14× (z +12.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[KATO III (line)]] | alt | 56.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +13.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +11.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[LS 180 (line)]] | wt | 25.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.97× (z +9.7) ⚠ cell-cycle shift, explains ~47% of this change | [[Selinexor (drug)]] 5 µM 0.264× (z -11.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 46.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.04× (z +13.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H23 (line)]] | alt | 52.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +10.4) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +12.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[Panc 03.27 (line)]] | alt | 37.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +11.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[PANC-1 (line)]] | alt | 35.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +12.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SNU-423 (line)]] | alt | 50.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +12.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SW1417 (line)]] | alt | 54.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +11.9) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[C32 (line)]] | wt | 31.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +9.9) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[HT-29 (line)]] | alt | 21.7 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.13× (z +8.7) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.57× (z +9.0) ⚠ cell-cycle shift, explains ~47% of this change | [[Selinexor (drug)]] 5 µM 0.218× (z -10.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 18.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +10.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[RKO (line)]] | wt | 55.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SW48 (line)]] | wt | 37.6 | 0 | 2 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.296× (z -9.9) |
| [[AN3 CA (line)]] | alt | 56.9 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0793× (z -11.0) |
| [[COLO 205 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.18× (z +9.5) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[HOP62 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.5) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 61.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +9.0) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SW 1271 (line)]] | alt | 43.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM 0.0555× (z -9.3) |
| [[SW 900 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.16× (z +9.2) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLM]] | +0.93 | +0.93 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CENPK]] | +0.92 | +0.93 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | STRING 454 |
| [[DTL]] | +0.89 | +0.91 / +0.87 | both halves | 7e-06 |  |
| [[SPC24]] | +0.88 | +0.85 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[POLQ]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 |  |
| [[MELK]] | +0.87 | +0.88 / +0.86 | both halves | 7e-06 |  |
| [[FANCI]] | +0.87 | +0.88 / +0.83 | both halves | 7e-06 | same gene group; pathway: Fanconi Anemia Pathway; STRING 999 |
| [[CDC45]] | +0.87 | +0.89 / +0.83 | both halves | 7e-06 |  |
| [[WDR76]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 |  |
| [[FANCA]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999 |
| [[NCAPG2]] | +0.86 | +0.87 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises FANCB's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without E2F8 | 0.030 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises FANCB's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib) | 50% of the class's compounds vs 3.6% of all compounds | 0.058 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers FANCB's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises FANCB's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[DSCC1]] | C | DSCC1 activity raises FANCB's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without DSCC1 | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises FANCB's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.56× lower at baseline in the lines without MYBL2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[PBK]] | C | PBK activity raises FANCB's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.45× lower at baseline in the lines without PBK | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.876). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.9, -46.3); signed map (-38.9, -43.2). **Vector** length 135, 44.9% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.63 to 65); *DNA strand elongation* (reactome, mean cos +0.69 to 28); *DNA Replication* (reactome, mean cos +0.70 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.1 | +26.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.2 | +29.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.9 | +26.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +5.5 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.3 | +7.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +6.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.8 | +2.7 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -10.9 | -11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.5 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.7 | -3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -8.0 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.5 | -0.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.6 | -4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:14,690,388-14,873,255 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAB, FLJ34064, FAAP95 |
| Gene groups (HGNC) | FA complementation groups; FA core complex |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB91](https://www.uniprot.org/uniprotkb/Q8NB91) (Fanconi anemia group B protein):

> DNA repair protein required for FANCD2 ubiquitination.

**Summary**, from NCBI Gene [2187](https://www.ncbi.nlm.nih.gov/gene/2187):

> This gene encodes a member of the Fanconi anemia complementation group B. This protein is assembled into a nucleoprotein complex that is involved in the repair of DNA lesions. Mutations in this gene can cause chromosome instability and VACTERL syndrome with hydrocephalus. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:3583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3583) · Entrez [2187](https://www.ncbi.nlm.nih.gov/gene/2187) · UniProt [Q8NB91](https://www.uniprot.org/uniprotkb/Q8NB91) · Ensembl [ENSG00000181544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181544)

## Data

Gene col 11195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11195); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11195]; `tensor/DDL_lfc|DDL_z.npy` [11195]; `embed/gene_vectors.npy` [11195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11195 or target_col == 11195). Every well: [[FANCB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
