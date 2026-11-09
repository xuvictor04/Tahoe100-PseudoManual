---
symbol: "REST"
type: "gene"
col: 1394
ensembl_id: "ENSG00000084093"
name: "RE1 silencing transcription factor"
location: "4q12"
module: 28
arm: "+"
pooled_cpm: 139.85
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# REST

*RE1 silencing transcription factor* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +24.9, q 0e+00, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.01× (z +18.6, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.661× (z -9.6, q 3e-19, down in 32 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 0.5 µM: 0.810× (z -3.7, q 0.010, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THAP1]] (+0.79, fdr 7e-06), [[RSF1]] (+0.76, fdr 7e-06), [[PPP1R12A]] (+0.71, fdr 7e-06); moves opposite to [[CHID1]] (-0.63, fdr 1e-05), [[SHQ1]] (-0.60, fdr 1e-05), [[RPSA]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IRX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.93×** | +24.9 | 0e+00 | 39/46 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +18.6 | 0e+00 | 44/46 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +17.1 | 0e+00 | 44/46 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +14.6 | 0e+00 | 43/46 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +12.6 | 3e-34 | 42/46 (HEC-1-A, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +11.6 | 3e-29 | 39/46 (HOP62, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +8.3 | 9e-15 | 27/47 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.35×** | +8.0 | 7e-14 | 32/46 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.32×** | +7.3 | 1e-11 | 29/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.23×** | +5.5 | 2e-06 | 25/46 (SW480, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.22×** | +5.2 | 8e-06 | 22/46 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +5.2 | 9e-06 | 22/46 (A-172, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.7 | 1e-04 | 24/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | ⚠ position correction uncertain | 1.18× | +4.4 | 5e-04 | 16/47 (KATO III, NCI-H2030, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.1 | 0.002 | 18/46 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.068 | 12/46 (A-427, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -9.6 | 3e-19 | 32/43 (SNU-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.718×** | -8.8 | 4e-16 | 33/47 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -7.4 | 2e-11 | 36/46 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.752×** | -7.3 | 5e-11 | 25/42 (Panc 03.27, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.764×** | -7.2 | 9e-11 | 26/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -6.0 | 2e-07 | 2/48 (HOP62, NCI-H2122) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.802×** | -5.9 | 4e-07 | 26/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.798×** | -5.6 | 2e-06 | 25/46 (HEC-1-A, CFPAC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.823×** | -5.2 | 1e-05 | 26/46 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.707×** | -4.8 | 8e-05 | 28/43 (NCI-H1573, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **0.828×** | -4.8 | 8e-05 | 24/45 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.856× | -4.1 | 0.002 | 16/46 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.810×** | -3.7 | 0.010 | 18/46 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.774×** | -3.6 | 0.015 | 18/46 (SNU-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.775×** | -3.5 | 0.015 | 19/46 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.776×** | -3.5 | 0.016 | 21/46 (SNU-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | 0.879× | -3.4 | 0.022 | 11/46 (SW 900, LoVo, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.882× | -3.3 | 0.027 | 13/46 (C32, HOP62, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.889× | -3.1 | 0.049 | 12/46 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.841× | -3.0 | 0.061 | 14/46 (SNU-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.922× | -3.0 | 0.064 | 1/46 (H4) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 151 | 8 (5 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +16.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.65× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.479× (z -14.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 186 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +23.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +19.0) | [[Lonafarnib (drug)]] 5 µM 0.390× (z -9.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 113 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 193 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -16.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 141 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +18.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.514× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.549× (z -9.1) |
| [[LS 180 (line)]] | wt | 134 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +19.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 140 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.15× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[RKO (line)]] | wt | 188 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.65× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -9.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 165 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +17.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +16.0) | [[Ixazomib citrate (drug)]] 5 µM 0.582× (z -8.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H23 (line)]] | alt | 179 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +21.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.08× (z +15.7) | — |
| [[NCI-H2347 (line)]] | alt | 160 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +15.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.459× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[SK-MEL-2 (line)]] | alt | 158 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.41× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -14.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 183 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -13.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 154 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +21.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +15.3) | — |
| [[A549 (line)]] | wt | 112 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +13.3) | — |
| [[AsPC-1 (line)]] | alt | 124 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.16× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -14.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 109 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.92× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 159 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.509× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 147 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +17.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.551× (z -9.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 137 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.448× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 149 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +15.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +13.7) | — |
| [[BT-474 (line)]] | alt | 139 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +14.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.417× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 130 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 144 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 136 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 2.10× (z +11.0) | — |
| [[SW48 (line)]] | wt | 163 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 173 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +11.0) | — |
| [[LoVo (line)]] | wt | 120 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.86× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -13.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 129 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.32× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 122 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -17.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 149 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.88× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -15.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 116 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 146 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.07× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 120 | 2 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 1.81× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 130 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 212 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.79× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 153 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 131 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.320× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 205 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 214 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP1]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[RSF1]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[PPP1R12A]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SCAF11]] | +0.71 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.71 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[TRMT1L]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 | same gene group |
| [[PDCD7]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TBCC]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[LINC02307]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[YY1]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHID1]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.60 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[RPSA]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[PRDX3]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[STRAP]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[OPA1]] | -0.59 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[PABIR2]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[FAM20B]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[EEF1AKMT2]] | -0.57 | -0.49 / -0.62 | both halves | 2e-05 |  |
| [[RBM14-RBM4]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TECR]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRX3]] | B | IRX3 activity raises REST's level | lines that do not express IRX3 (9) vs lines expressing it (41) | 1.60× lower at baseline in the lines without IRX3 | 0.098 | ⚠ within organs, on part of the lines; also absent: DYSF, DRAM1, LINC02609 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.431). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-36.5, 4.0); signed map (3.9, -15.6). **Vector** length 138, 42.9% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.1 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.0 | +18.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.3 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +8.6 | +24.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +17.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +11.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.9 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +5.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -7.1 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.3 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | RE1 silencing transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,907,876-56,966,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NRSF, XBR; previously DFNA27 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 18 pathways, smallest: Regulation of NPAS4 gene transcription; Regulation of NPAS4 gene expression; Transcriptional Regulation by NPAS4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13127](https://www.uniprot.org/uniprotkb/Q13127) (RE1-silencing transcription factor):

> Transcriptional repressor which binds neuron-restrictive silencer element (NRSE) and represses neuronal gene transcription in non-neuronal cells. Restricts the expression of neuronal genes by associating with two distinct corepressors, SIN3A and RCOR1, which in turn recruit histone deacetylase to the promoters of REST-regulated genes. Mediates repression by recruiting the BHC complex at RE1/NRSE sites which acts by deacetylating and demethylating specific sites on histones, thereby acting as a …

**Summary**, from NCBI Gene [5978](https://www.ncbi.nlm.nih.gov/gene/5978):

> This gene was initially identified as a transcriptional repressor that represses neuronal genes in non-neuronal tissues. However, depending on the cellular context, this gene can act as either an oncogene or a tumor suppressor. The encoded protein is a member of the Kruppel-type zinc finger transcription factor family. It represses transcription by binding a DNA sequence element called the neuron-restrictive silencer element. The protein is also found in undifferentiated neuronal progenitor …

**Accessions** — [HGNC:9966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9966) · Entrez [5978](https://www.ncbi.nlm.nih.gov/gene/5978) · UniProt [Q13127](https://www.uniprot.org/uniprotkb/Q13127) · Ensembl [ENSG00000084093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084093)

## Data

Gene col 1394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1394); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1394]; `tensor/DDL_lfc|DDL_z.npy` [1394]; `embed/gene_vectors.npy` [1394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1394 or target_col == 1394). Every well: [[REST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
