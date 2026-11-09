---
symbol: "N4BP2L2"
type: "gene"
col: 14416
ensembl_id: "ENSG00000244754"
name: "NEDD4 binding protein 2 like 2"
location: "13q13.1"
module: 149
arm: "+"
pooled_cpm: 293.27
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# N4BP2L2

*NEDD4 binding protein 2 like 2* — 13q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.35× (z +7.0, q 1e-09, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.304× (z -27.9, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.600× (z -12.0, q 4e-31, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC59]] (+0.78, fdr 7e-06), [[GTF2IRD2B]] (+0.72, fdr 8e-06), [[ANKHD1-EIF4EBP3]] (+0.71, fdr 1e-05); moves opposite to [[COLGALT1]] (-0.64, fdr 1e-05), [[BLTP2]] (-0.64, fdr 3e-05), [[SKP2]] (-0.63, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GPALPP1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +7.0 | 1e-09 | 36/48 (C-33 A, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +5.4 | 2e-05 | 31/47 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 9e-04 | 29/48 (KATO III, J82, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.67×** | +4.3 | 0.003 | 32/49 (A-427, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 1.13× | +4.2 | 0.003 | 9/48 (HCT15, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.29×** | +4.0 | 0.005 | 27/50 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.9 | 0.007 | 21/48 (C-33 A, HEC-1-A, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.12× | +3.9 | 0.007 | 4/49 (C32, Hs 766T, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.8 | 0.009 | 9/48 (C-33 A, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.8 | 0.009 | 7/49 (Hs 766T, LoVo, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.011 | 23/50 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.6 | 0.014 | 11/48 (LoVo, Hs 766T, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.014 | 12/48 (A498, C-33 A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.014 | 15/49 (SNU-1, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.015 | 12/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.015 | 23/49 (LS 180, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.015 | 15/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.11× | +3.3 | 0.025 | 7/48 (Hs 766T, SW48, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.304×** | -27.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.346×** | -24.9 | 0e+00 | 48/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.363×** | -23.8 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.495×** | -15.2 | 0e+00 | 40/45 (A-427, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.540×** | -14.4 | 4e-45 | 42/49 (COLO 205, SNU-423, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.600×** | -12.0 | 4e-31 | 46/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **0.622×** | -10.7 | 8e-25 | 35/44 (HT-29, Hs 766T, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.725×** | -10.7 | 1e-24 | 38/49 (A-172, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.684×** | -8.9 | 3e-17 | 36/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.695×** | -8.5 | 9e-16 | 41/48 (H4, COLO 205, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.698×** | -8.1 | 3e-14 | 39/47 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **0.719×** | -7.4 | 5e-12 | 33/47 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.803×** | -7.2 | 2e-11 | 33/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -6.0 | 1e-07 | 29/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.560×** | -4.8 | 6e-05 | 25/38 (SK-MEL-2, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.578×** | -4.5 | 2e-04 | 35/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.040 | 15/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | 0.878× | -3.0 | 0.069 | 8/48 (MIA PaCa-2, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 265 | 2 (2 ⚠) | 13 (12 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.259× (z -23.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.599× (z -9.0) |
| [[PANC-1 (line)]] | alt | 260 | 0 | 12 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -23.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.552× (z -10.9) |
| [[HT-29 (line)]] | alt | 627 | 0 | 11 (10 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -20.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.533× (z -9.6) |
| [[SNU-423 (line)]] | alt | 342 | 0 | 11 (10 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -19.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.510× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 270 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -19.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.526× (z -9.5) |
| [[Hs 766T (line)]] | wt | 469 | 0 | 9 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -18.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 311 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -19.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.522× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 332 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -16.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.504× (z -9.8) |
| [[SW480 (line)]] | alt | 361 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -24.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.496× (z -12.1) |
| [[A-172 (line)]] | wt | 245 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -19.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.572× (z -8.9) |
| [[COLO 205 (line)]] | alt | 1,241 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -23.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.462× (z -11.9) |
| [[LoVo (line)]] | wt | 337 | 2 (2 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.330× (z -19.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 302 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -21.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 287 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -18.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.405× (z -9.6) |
| [[KATO III (line)]] | alt | 358 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -16.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 315 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -18.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.538× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 455 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -20.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.573× (z -8.6) |
| [[A498 (line)]] | wt | 217 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -16.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 249 | 1 | 5 (5 ⚠) | [[Auranofin (drug)]] 5 µM 1.93× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.432× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 250 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -17.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 222 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -17.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 266 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -12.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 317 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 635 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -18.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 395 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -20.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.589× (z -8.7) |
| [[J82 (line)]] | alt | 331 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.370× (z -16.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 187 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -13.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 388 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -15.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 170 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 257 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -16.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 233 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -15.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 168 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -13.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 232 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -12.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 342 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -14.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 154 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -16.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 134 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.423× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 268 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -15.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 1271 (line)]] | alt | 630 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -13.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 266 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.295× (z -14.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 242 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.315× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[AsPC-1 (line)]] | alt | 170 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -15.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 392 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 139 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -9.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 202 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -16.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 187 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.510× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2122 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 350 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC59]] | +0.78 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[GTF2IRD2B]] | +0.72 | +0.73 / +0.57 | both halves | 8e-06 |  |
| [[ANKHD1-EIF4EBP3]] | +0.71 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[MAU2]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TSC1]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MRPL45P2]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.69 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[C11orf58]] | +0.69 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[C1orf43]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NKAPD1]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[N4BP2L1]] | +0.68 | +0.63 / +0.57 | both halves | 1e-05 | ⚠ **readthrough risk**: N4BP2L1 lies 4.1 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ASH1L]] | +0.68 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.68 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLGALT1]] | -0.64 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.64 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[SKP2]] | -0.63 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[WASF3]] | -0.63 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[GLB1L2]] | -0.62 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[PODXL2]] | -0.62 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SDHAF3]] | -0.61 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[METAP1]] | -0.61 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[DAG1]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PARP1]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[APMAP]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TUBG1]] | -0.60 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPALPP1]] | C | GPALPP1's natural level strengthens N4BP2L2's drug response | GPALPP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.68, reverse -0.07; direction clear | 0.015 | ⚠ tissue can mimic it; precision caveat |
| [[ANKRD49]] | C | ANKRD49's natural level strengthens N4BP2L2's drug response | ANKRD49's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.21; direction not clear | 0.042 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[WBP4]] | C | WBP4's natural level strengthens N4BP2L2's drug response | WBP4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.14; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.5, 15.5); signed map (-0.8, -6.1). **Vector** length 136, 54.1% of its response variance represented; |z| ≥ 3 in 1,431 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +9.7 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.4 | +4.3 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -7.1 | -12.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.0 | -23.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.4 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.5 | -27.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.3 | -4.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.8 | -1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | NEDD4 binding protein 2 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.1 — chr13:32,432,417-32,538,885 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CG005, PFAAP5 |
| Matched by | ensembl_id |

UniProt [Q92802](https://www.uniprot.org/uniprotkb/Q92802) carries no function annotation.

**Summary**, from NCBI Gene [10443](https://www.ncbi.nlm.nih.gov/gene/10443):

> Enables enzyme binding activity. Involved in negative regulation of hematopoietic stem cell differentiation and positive regulation of hematopoietic stem cell proliferation. Located in nucleus. Part of transcription repressor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26916) · Entrez [10443](https://www.ncbi.nlm.nih.gov/gene/10443) · UniProt [Q92802](https://www.uniprot.org/uniprotkb/Q92802) · Ensembl [ENSG00000244754](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244754)

## Data

Gene col 14416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14416); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14416]; `tensor/DDL_lfc|DDL_z.npy` [14416]; `embed/gene_vectors.npy` [14416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14416 or target_col == 14416). Every well: [[N4BP2L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/N4BP2L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
