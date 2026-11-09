---
symbol: "WDR62"
type: "gene"
col: 1129
ensembl_id: "ENSG00000075702"
name: "WD repeat domain 62"
location: "19q13.12"
module: 67
arm: "+"
pooled_cpm: 28.09
n_lines_expressing: 48
n_dd_up: 31
n_dd_down: 30
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# WDR62

*WD repeat domain 62* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (24 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.12× (z +16.6, q 0e+00, up in 41 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.71× (z +7.8, q 2e-13, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.430× (z -17.6, q 0e+00, down in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.739× (z -4.9, q 1e-04, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPN]] (+0.88, fdr 7e-06), [[MELK]] (+0.86, fdr 7e-06), [[ORC6]] (+0.84, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 24 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.12×** | +16.6 | 0e+00 | 41/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **3.06×** | +16.4 | 0e+00 | 43/46 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.98×** | +14.1 | 1e-42 | 33/46 (A549, RKO, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.57×** | +13.8 | 3e-41 | 42/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.54×** | +13.7 | 2e-40 | 39/46 (SW480, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **2.53×** | +13.6 | 4e-40 | 38/46 (SW480, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.51×** | +13.5 | 2e-39 | 41/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **2.30×** | +12.2 | 4e-32 | 34/45 (SW480, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **2.23×** | +11.3 | 1e-27 | 39/44 (NCI-H460, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.15×** | +10.7 | 4e-25 | 33/46 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.59×** | +9.5 | 8e-20 | 31/45 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.83×** | +8.9 | 4e-17 | 37/45 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.78×** | +8.4 | 2e-15 | 32/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.78×** | +8.1 | 2e-14 | 27/46 (C32, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.75×** | +7.8 | 2e-13 | 28/45 (C32, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +7.8 | 2e-13 | 29/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +7.7 | 6e-13 | 31/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.0 | 2e-05 | 20/45 (NCI-H460, H4, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.010 | 10/45 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.022 | 12/43 (SW 900, A549, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.037 | 14/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.045 | 9/45 (SW480, J82, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.430×** | -17.6 | 0e+00 | 41/46 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.417×** | -12.9 | 2e-35 | 39/45 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.600×** | -7.5 | 9e-12 | 35/46 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.669×** | -5.9 | 4e-07 | 28/44 (HT-29, H4, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.677×** | -5.8 | 1e-06 | 21/44 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.739×** | -4.9 | 1e-04 | 18/46 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.741×** | -4.4 | 7e-04 | 18/45 (NCI-H460, A-172, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.812×** | -4.4 | 9e-04 | 17/46 (COLO 205, Hs 766T, …) | two highest doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.571×** | -4.3 | 0.001 | 18/43 (H4, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | **0.743×** | -4.2 | 0.001 | 16/45 (C32, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.751×** | -4.1 | 0.002 | 17/44 (HCT15, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.750×** | -4.1 | 0.002 | 17/46 (A-427, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.752×** | -4.1 | 0.002 | 15/45 (A498, PANC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.600×** | -3.9 | 0.003 | 14/45 (H4, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.691×** | -3.9 | 0.004 | 12/46 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.004 | 19/46 (SHP-77, LS 180, …) | all doses, stronger at high dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.606×** | -3.9 | 0.004 | 16/42 (H4, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.722×** | -3.4 | 0.017 | 14/46 (SW480, SW 1271, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.648×** | -3.3 | 0.022 | 12/43 (A-172, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.858× | -3.2 | 0.031 | 14/46 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.867× | -3.0 | 0.058 | 13/46 (PANC-1, Hs 766T, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.814×** | -3.0 | 0.058 | 13/46 (A-427, H4, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.06 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.3 | 10 (10 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 4.30× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Selinexor (drug)]] 0.5 µM 0.288× (z -11.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[H4 (line)]] | wt | 47.1 | 2 (2 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.42× (z +8.7) ⚠ cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0413× (z -16.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.204× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 20.7 | 7 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +14.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.35× (z +8.9) | [[Selinexor (drug)]] 0.5 µM 0.269× (z -9.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A549 (line)]] | wt | 30.2 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +15.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 52.8 | 5 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +11.0) ⚠ cell-cycle shift, explains ~41% of this change | [[Selinexor (drug)]] 5 µM 0.358× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 66.1 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 31.6 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.193× (z -16.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.411× (z -8.7) |
| [[J82 (line)]] | alt | 57.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.7) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.8 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.189× (z -14.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 65.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.146× (z -21.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 11.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.49× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.208× (z -11.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 51.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.6) ⚠ cell-cycle shift, explains ~40% of this change | [[Selinexor (drug)]] 5 µM 0.322× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 7.89 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +13.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +11.8) ⚠ cell-cycle shift, explains ~40% of this change | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.120× (z -10.5) |
| [[SHP-77 (line)]] | alt | 61.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.23× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 11.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SW1417 (line)]] | alt | 25.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.8) ⚠ cell-cycle shift, explains ~40% of this change | [[Selinexor (drug)]] 5 µM 0.330× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.232× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.221× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.284× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 9.95 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.75× (z +9.1) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.188× (z -15.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +8.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +8.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +15.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.327× (z -11.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0765× (z -11.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPN]] | +0.88 | +0.88 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[MELK]] | +0.86 | +0.85 / +0.86 | both halves | 7e-06 |  |
| [[ORC6]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[POLQ]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[CENPO]] | +0.83 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[CDCA5]] | +0.83 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[AURKB]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | STRING 525 |
| [[HAUS8]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SPC24]] | +0.82 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[SPC25]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[RRM2]] | +0.81 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[FANCA]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises WDR62's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises WDR62's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.73× lower at baseline in the lines without CDC25A | 0.066 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers WDR62's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CENPP]] | C | CENPP activity raises WDR62's level | lines that do not express CENPP (4) vs lines expressing it (46) | 3.34× lower at baseline in the lines without CENPP | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises WDR62's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.08× lower at baseline in the lines without PBK | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises WDR62's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.78× lower at baseline in the lines without AURKB | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[E2F1]] | C | E2F1 activity raises WDR62's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 2.98× lower at baseline in the lines without E2F1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.7, -48.3); signed map (-41.4, -43.7). **Vector** length 122, 39.6% of its response variance represented; |z| ≥ 3 in 1,475 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.73 to 12); *G2/M checkpoint* (hallmark, mean cos +0.75 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.68 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.8 | +8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.7 | +13.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.1 | +13.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +4.0 | +16.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.1 | +16.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -13.4 | -17.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -9.8 | -12.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.9 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +2.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 62 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,054,649-36,105,108 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434J046, FLJ33298; previously C19orf14, MCPH2 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43379](https://www.uniprot.org/uniprotkb/O43379) (WD repeat-containing protein 62):

> Required for cerebral cortical development. Plays a role in neuronal proliferation and migration. Plays a role in mother-centriole-dependent centriole duplication; the function also seems to involve CEP152, CDK5RAP2 and CEP63 through a stepwise assembled complex at the centrosome that recruits CDK2 required for centriole duplication.

**Summary**, from NCBI Gene [284403](https://www.ncbi.nlm.nih.gov/gene/284403):

> This gene is proposed to play a role in cerebral cortical development. Mutations in this gene have been associated with microencephaly, cortical malformations, and cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:24502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24502) · Entrez [284403](https://www.ncbi.nlm.nih.gov/gene/284403) · UniProt [O43379](https://www.uniprot.org/uniprotkb/O43379) · Ensembl [ENSG00000075702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075702)

## Data

Gene col 1129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1129); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1129]; `tensor/DDL_lfc|DDL_z.npy` [1129]; `embed/gene_vectors.npy` [1129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1129 or target_col == 1129). Every well: [[WDR62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
