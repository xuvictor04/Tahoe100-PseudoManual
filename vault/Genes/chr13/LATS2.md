---
symbol: "LATS2"
type: "gene"
col: 7436
ensembl_id: "ENSG00000150457"
name: "large tumor suppressor kinase 2"
location: "13q12.11"
module: 123
arm: "+"
pooled_cpm: 118.26
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 33
n_dd_up_clean: 14
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# LATS2

*large tumor suppressor kinase 2* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.69× (z +26.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.527× (z -11.8, q 2e-29, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.464× (z -7.4, q 1e-11, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMOTL2]] (+0.84, fdr 7e-06), [[EDN1]] (+0.66, fdr 1e-05), [[LINC01836]] (+0.64, fdr 1e-05); moves opposite to [[GRB10]] (-0.53, fdr 3e-05), [[UBA6]] (-0.50, fdr 7e-05), [[KIF21B]] (-0.50, fdr 1e-04).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CCN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +26.0 | 0e+00 | 46/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.16×** | +17.6 | 0e+00 | 47/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.46×** | +16.7 | 0e+00 | 45/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +11.4 | 8e-28 | 34/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +11.1 | 1e-26 | 42/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +10.5 | 9e-24 | 39/47 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +10.0 | 9e-22 | 44/47 (SW480, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +9.9 | 2e-21 | 40/47 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +8.7 | 2e-16 | 36/47 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 7e-06 | 25/47 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +5.2 | 8e-06 | 29/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +5.1 | 2e-05 | 24/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +4.5 | 4e-04 | 22/49 (NCI-H460, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 8e-04 | 23/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.20× | +4.0 | 0.003 | 18/47 (NCI-H460, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.006 | 12/47 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.017 | 14/49 (NCI-H23, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.527×** | -11.8 | 2e-29 | 39/47 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.541×** | -11.3 | 2e-27 | 41/47 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.534×** | -10.7 | 2e-24 | 35/44 (C-33 A, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.571×** | -10.3 | 8e-23 | 33/48 (RKO, LoVo, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.574×** | -10.2 | 2e-22 | 40/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.589×** | -9.8 | 2e-20 | 39/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.601×** | -9.0 | 2e-17 | 27/43 (SNU-1, SW48, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.464×** | -7.4 | 1e-11 | 39/47 (SW1417, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.676×** | -6.9 | 3e-10 | 32/46 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.694×** | -6.7 | 1e-09 | 28/47 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.700×** | -6.5 | 3e-09 | 30/46 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.728×** | -5.8 | 3e-07 | 30/47 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -5.7 | 6e-07 | 28/47 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.664×** | -5.4 | 3e-06 | 33/47 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.574×** | -5.4 | 3e-06 | 27/47 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.588×** | -5.1 | 1e-05 | 34/47 (SW480, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.785×** | -4.2 | 7e-04 | 24/47 (SNU-1, LoVo, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.797×** | -4.1 | 8e-04 | 24/47 (KATO III, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.658×** | -4.0 | 0.001 | 23/47 (Panc 03.27, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **0.799×** | -3.8 | 0.003 | 19/46 (C-33 A, SNU-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.006 | 19/48 (SW480, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.694×** | -3.5 | 0.009 | 21/46 (HCT15, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.874× | -3.5 | 0.010 | 10/48 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 237 | 5 | 8 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 147 | 10 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +24.8) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 92.0 | 8 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +18.0) | [[Panobinostat (drug)]] 0.5 µM 0.499× (z -9.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 207 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 0.382× (z -8.8) |
| [[SNU-1 (line)]] | wt | 252 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.16× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.0623× (z -26.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 54.7 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.32× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.261× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 129 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +23.8) | — |
| [[NCI-H23 (line)]] | alt | 300 | 1 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 7.81× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.127× (z -18.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 154 | 2 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 8.46× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.239× (z -15.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[C32 (line)]] | wt | 39.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +17.4) | — |
| [[HEC-1-A (line)]] | alt | 133 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[J82 (line)]] | alt | 274 | 3 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 8.93× (z +14.7) | [[Selinexor (drug)]] 5 µM 0.506× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 114 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -9.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 118 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +13.7) | — |
| [[LoVo (line)]] | wt | 116 | 1 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 45.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +18.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 133 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +21.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.390× (z -8.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 170 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.429× (z -10.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HOP62 (line)]] | alt | 86.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 44.0 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +16.6) | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 200 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 69.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.8) | — |
| [[RKO (line)]] | wt | 179 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 130 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -20.2) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW48 (line)]] | wt | 88.1 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0904× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 140 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.337× (z -11.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HCT15 (line)]] | alt | 97.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 108 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 90.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +16.5) | — |
| [[COLO 205 (line)]] | alt | 48.9 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.45× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 120 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 95.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.276× (z -9.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 66.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +14.9) | — |
| [[SK-MEL-2 (line)]] | alt | 56.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +15.8) | — |
| [[HepG2_C3A (line)]] | wt | 89.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 226 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0800× (z -10.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 81.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 98.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +16.2) | — |
| [[AN3 CA (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 82.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +12.2) | — |
| [[H4 (line)]] | wt | 58.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.3) | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0713× (z -11.8) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 80.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMOTL2]] | +0.84 | +0.81 / +0.80 | both halves | 7e-06 | pathway: Signaling by Hippo; STRING 934 |
| [[EDN1]] | +0.66 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LINC01836]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TGFB2]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[AJUBA]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 | STRING 983 |
| [[ARHGEF17]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ERBIN]] | +0.60 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[CCN1]] | +0.58 | +0.59 / +0.64 | both halves | 7e-06 | STRING 651 |
| [[TGIF2]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[FOSL2]] | +0.58 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[CFLAR-AS1]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ARID5B]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB10]] | -0.53 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[UBA6]] | -0.50 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[KIF21B]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.50 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[NBPF3]] | -0.50 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[EIF4EBP1]] | -0.49 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ITPR1]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ATP2C1]] | -0.48 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[TMEM255B]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NQO2]] | -0.48 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[STX1A]] | -0.47 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[OTULIN]] | -0.47 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN1]] | B | CCN1 activity raises LATS2's level | lines that do not express CCN1 (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without CCN1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CTSL, ENSG00000232295, EBI3 |
| [[ST6GALNAC5]] | B | ST6GALNAC5 activity lowers LATS2's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.64× higher at baseline in the lines without ST6GALNAC5 | 0.047 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[RIMKLB]] | B | RIMKLB activity raises LATS2's level | lines that do not express RIMKLB (13) vs lines expressing it (37) | 1.25× lower at baseline in the lines without RIMKLB | 0.075 | ⚠ within organs, on part of the lines; also absent: DNAAF9, GJC1, ANKRD6 |
| [[DDAH1]] | C | DDAH1 activity raises LATS2's level | lines that do not express DDAH1 (3) vs lines expressing it (47) | 3.56× lower at baseline in the lines without DDAH1 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: MMP25, KDELR3, BCL2L1; maybe low, not absent |
| [[RBMS2]] | C | RBMS2 activity raises LATS2's level | lines that do not express RBMS2 (3) vs lines expressing it (47) | 3.97× lower at baseline in the lines without RBMS2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HOMER3, ARHGAP10, TMEM144; maybe low, not absent; its own permutation p |
| [[AMOTL2]] | C | AMOTL2 activity raises LATS2's level | lines that do not express AMOTL2 (4) vs lines expressing it (46) | 3.85× lower at baseline in the lines without AMOTL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: BCL2L1, RASSF7, FCHO1; its own permutation p |
| [[ARHGEF17]] | C | ARHGEF17 activity raises LATS2's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without ARHGEF17 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, 12.7); signed map (48.8, 14.9). **Vector** length 142, 50.8% of its response variance represented; |z| ≥ 3 in 1,629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +26.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +17.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.7 | +4.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +5.5 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +11.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.2 | +5.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.8 | +2.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.6 | +2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +4.3 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.0 | -10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -8.5 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -7.5 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.4 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.2 | -7.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.1 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.3 | -5.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | -5.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | large tumor suppressor kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:20,973,036-21,061,586 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Large tumor suppressor kinase family |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRM7](https://www.uniprot.org/uniprotkb/Q9NRM7) (Serine/threonine-protein kinase LATS2):

> Negative regulator of YAP1 in the Hippo signaling pathway that plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein STK3/MST2 and STK4/MST1, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. Phosphorylation of YAP1 …

**Summary**, from NCBI Gene [26524](https://www.ncbi.nlm.nih.gov/gene/26524):

> This gene encodes a serine/threonine protein kinase belonging to the LATS tumor suppressor family. The protein localizes to centrosomes during interphase, and early and late metaphase. It interacts with the centrosomal proteins aurora-A and ajuba and is required for accumulation of gamma-tubulin and spindle formation at the onset of mitosis. It also interacts with a negative regulator of p53 and may function in a positive feedback loop with p53 that responds to cytoskeleton damage. …

**Accessions** — [HGNC:6515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6515) · Entrez [26524](https://www.ncbi.nlm.nih.gov/gene/26524) · UniProt [Q9NRM7](https://www.uniprot.org/uniprotkb/Q9NRM7) · Ensembl [ENSG00000150457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150457)

## Data

Gene col 7436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7436); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7436]; `tensor/DDL_lfc|DDL_z.npy` [7436]; `embed/gene_vectors.npy` [7436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7436 or target_col == 7436). Every well: [[LATS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LATS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
