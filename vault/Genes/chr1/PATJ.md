---
symbol: "PATJ"
type: "gene"
col: 5385
ensembl_id: "ENSG00000132849"
name: "PATJ crumbs cell polarity complex component"
location: "1p31.3"
module: 31
arm: "+"
pooled_cpm: 311.42
n_lines_expressing: 41
n_dd_up: 5
n_dd_down: 35
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 19
direction_downstream: 17
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PATJ

*PATJ crumbs cell polarity complex component* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.21× (z +4.1, q 0.014, up in 20 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (25 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.326× (z -23.6, q 0e+00, down in 39 of 39 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.584× (z -15.9, q 0e+00, down in 37 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP7]] (+0.53, fdr 2e-05), [[STAU2]] (+0.52, fdr 3e-05), [[FAM83B]] (+0.52, fdr 6e-05); moves opposite to [[ZNF521]] (-0.56, fdr 2e-05), [[INSYN2B]] (-0.53, fdr 4e-05), [[TSHZ3]] (-0.50, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TMC4]] → it (grade B ⚠); 17 go from it, the strongest it → [[PRRX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.014 | 20/38 (NCI-H2030, SW48, …) | rises with dose | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.014 | 18/39 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.014 | 17/38 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.9 | 0.014 | 6/39 (H4, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.21×** | +3.8 | 0.014 | 19/38 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.015 | 22/41 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.5 | 0.032 | 3/39 (NCI-H661, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 1.19× | +3.5 | 0.033 | 17/41 (SNU-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 28 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.326×** | -23.6 | 0e+00 | 39/39 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.337×** | -22.9 | 0e+00 | 39/39 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.366×** | -21.1 | 0e+00 | 39/39 (NCI-H23, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.380×** | -19.6 | 0e+00 | 37/38 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.458×** | -16.4 | 0e+00 | 37/39 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -15.9 | 0e+00 | 37/40 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.511×** | -14.1 | 3e-43 | 34/39 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.294×** | -13.5 | 2e-39 | 39/40 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.659×** | -12.4 | 3e-33 | 31/39 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.569×** | -11.8 | 2e-30 | 30/39 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -11.3 | 4e-28 | 34/39 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.606×** | -10.5 | 4e-24 | 31/39 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.616×** | -9.8 | 5e-21 | 31/39 (COLO 205, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -9.7 | 1e-20 | 31/39 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.656×** | -8.8 | 4e-17 | 34/39 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.602×** | -5.6 | 5e-07 | 31/40 (A549, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -4.0 | 0.001 | 23/39 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.706×** | -3.8 | 0.002 | 22/39 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.896× | -3.2 | 0.021 | 14/39 (A-427, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.849× | -3.2 | 0.026 | 12/38 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.866× | -3.0 | 0.043 | 11/40 (RKO, A549, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.904× | -3.0 | 0.045 | 2/39 (CFPAC-1, NCI-H2347) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.827×** | -2.8 | 0.067 | 8/39 (NCI-H23, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.909× | -2.8 | 0.072 | 12/39 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.876× | -2.7 | 0.081 | 13/39 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 289 | 0 | 22 (17 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -24.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.315× (z -14.1) |
| [[SW480 (line)]] | alt | 362 | 0 | 22 (18 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -24.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -23.8) |
| [[CFPAC-1 (line)]] | alt | 681 | 0 | 19 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -24.2) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 757 | 0 | 19 (14 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -27.7) |
| [[NCI-H460 (line)]] | wt | 158 | 0 | 19 (15 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -19.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.374× (z -13.3) |
| [[LS 180 (line)]] | wt | 666 | 0 | 18 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -21.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -20.0) |
| [[NCI-H23 (line)]] | alt | 335 | 0 | 18 (15 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -26.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.145× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 752 | 0 | 17 (14 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -29.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.111× (z -18.2) |
| [[KATO III (line)]] | alt | 458 | 0 | 14 (12 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -24.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -23.8) |
| [[LoVo (line)]] | wt | 662 | 0 | 14 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -16.7) |
| [[PANC-1 (line)]] | alt | 232 | 0 | 14 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -11.8) |
| [[COLO 205 (line)]] | alt | 670 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -27.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -16.1) |
| [[HCT15 (line)]] | alt | 920 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -22.6) |
| [[HT-29 (line)]] | alt | 722 | 0 | 13 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -23.2) |
| [[SW48 (line)]] | wt | 477 | 0 | 13 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 320 | 0 | 12 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -20.0) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.380× (z -13.9) |
| [[HOP62 (line)]] | alt | 140 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -16.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 583 | 0 | 11 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.218× (z -21.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -14.3) |
| [[SNU-1 (line)]] | wt | 195 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -14.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.296× (z -11.0) |
| [[RKO (line)]] | wt | 113 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -22.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -12.1) |
| [[BT-474 (line)]] | alt | 539 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -19.0) |
| [[H4 (line)]] | wt | 146 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.295× (z -12.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.404× (z -9.1) |
| [[Hs 766T (line)]] | wt | 138 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -15.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.349× (z -9.6) |
| [[A-427 (line)]] | wt | 323 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -21.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.250× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 299 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -15.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.245× (z -8.6) |
| [[SNU-423 (line)]] | alt | 105 | 0 | 7 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.212× (z -16.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 195 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -22.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -18.5) |
| [[AsPC-1 (line)]] | alt | 281 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -13.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 447 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -18.0) |
| [[A-172 (line)]] | wt | 113 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -13.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.260× (z -8.6) |
| [[A498 (line)]] | wt | 174 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.425× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -11.1) |
| [[C-33 A (line)]] | alt | 148 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.392× (z -10.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 352 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -14.4) |
| [[SW 900 (line)]] | alt | 112 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -11.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.397× (z -10.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 25.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 70.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 50.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 58.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 31.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 60.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP7]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[STAU2]] | +0.52 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[FAM83B]] | +0.52 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[ARHGEF3]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PAX8-AS1]] | +0.50 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[RALGAPA1]] | +0.50 | +0.37 / +0.40 | both halves | 9e-05 |  |
| [[ANXA3]] | +0.49 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TTC39A]] | +0.48 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[NPIPB4]] | +0.48 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[MROH3P]] | +0.48 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[MYO5C]] | +0.47 | +0.41 / +0.39 | both halves | 5e-05 | same gene group |
| [[MYO1D]] | +0.47 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF521]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[INSYN2B]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TSHZ3]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[PRR16]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SDHAF3]] | -0.50 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[FZD1]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SRPX]] | -0.50 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[DZIP1L]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[PRICKLE2]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[WNT5A]] | -0.50 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[PTGFR]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[WHAMMP1]] | -0.49 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC4]] | B | TMC4 activity raises PATJ's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 3.84× lower at baseline in the lines without TMC4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[INAVA]], [[MROH3P]] | B | INAVA, MROH3P activity raises PATJ's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.35× lower at baseline in the lines without INAVA, MROH3P | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[CDH1]] | B | CDH1 activity raises PATJ's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.35× lower at baseline in the lines without CDH1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[MYO5B]] | B | MYO5B activity raises PATJ's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.50× lower at baseline in the lines without MYO5B | 5e-04 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[FAM83B]] | B | FAM83B activity raises PATJ's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.52× lower at baseline in the lines without FAM83B | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[OCLN]] | B | OCLN activity raises PATJ's level | lines that do not express OCLN (19) vs lines expressing it (31) | 3.73× lower at baseline in the lines without OCLN | 0.002 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[ANXA3]] | B | ANXA3 activity raises PATJ's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.21× lower at baseline in the lines without ANXA3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[DAPP1]] | B | DAPP1 activity raises PATJ's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.05× lower at baseline in the lines without DAPP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[CLDN4]] | B | CLDN4 activity raises PATJ's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 3.54× lower at baseline in the lines without CLDN4 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[LINC03047]] | B | LINC03047 activity lowers PATJ's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 3.36× higher at baseline in the lines without LINC03047 | 0.013 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |
| [[MAP7]] | B | MAP7 activity raises PATJ's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 3.52× lower at baseline in the lines without MAP7 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[PRR16]] | B | PRR16 activity lowers PATJ's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 3.26× higher at baseline in the lines without PRR16 | 0.028 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRX1]] | B | PATJ activity lowers PRRX1's level | lines that do not express PATJ (9) vs lines expressing it (41) | 11.22× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[RARB]] | B | PATJ activity lowers RARB's level | lines that do not express PATJ (9) vs lines expressing it (41) | 8.67× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[INSYN2B]] | B | PATJ activity lowers INSYN2B's level | lines that do not express PATJ (9) vs lines expressing it (41) | 7.50× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[LINC03047]] | B | PATJ activity lowers LINC03047's level | lines that do not express PATJ (9) vs lines expressing it (41) | 7.45× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[CSPG4]] | B | PATJ activity lowers CSPG4's level | lines that do not express PATJ (9) vs lines expressing it (41) | 6.23× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[SRPX]] | B | PATJ activity lowers SRPX's level | lines that do not express PATJ (9) vs lines expressing it (41) | 6.08× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[PTGFR]] | B | PATJ activity lowers PTGFR's level | lines that do not express PATJ (9) vs lines expressing it (41) | 4.57× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[EDNRA]] | B | PATJ activity lowers EDNRA's level | lines that do not express PATJ (9) vs lines expressing it (41) | 3.94× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[LOX]] | B | PATJ activity lowers LOX's level | lines that do not express PATJ (9) vs lines expressing it (41) | 3.82× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[ANPEP]] | B | PATJ activity lowers ANPEP's level | lines that do not express PATJ (9) vs lines expressing it (41) | 2.55× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[ZNF883]] | B | PATJ activity lowers ZNF883's level | lines that do not express PATJ (9) vs lines expressing it (41) | 2.47× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[FAM20C]] | B | PATJ activity lowers FAM20C's level | lines that do not express PATJ (9) vs lines expressing it (41) | 2.35× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.380). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.9, 22.2); signed map (53.8, 7.1). **Vector** length 99.5, 36.5% of its response variance represented; |z| ≥ 3 in 1,448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +5.1 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | -0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.0 | -12.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.8 | -9.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +4.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -19.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -11.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | -4.1 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.8 | -6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -9.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | PATJ crumbs cell polarity complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:61,742,477-62,178,675 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cipp; previously INADL |
| Gene groups (HGNC) | PDZ domain containing; Crumbs complex components; MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: SARS-CoV-2 targets PDZ proteins in cell-cell junction; Tight junction interactions; SARS-CoV-2-host interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI35](https://www.uniprot.org/uniprotkb/Q8NI35) (InaD-like protein):

> Scaffolding protein that facilitates the localization of proteins to the cell membrane. Required for the correct formation of tight junctions and epithelial apico-basal polarity. Acts (via its L27 domain) as an apical connector and elongation factor for multistranded TJP1/ZO1 condensates that form a tight junction belt, thereby required for the formation of the tight junction-mediated cell barrier (By similarity). Positively regulates epithelial cell microtubule elongation and cell migration, …

**Summary**, from NCBI Gene [10207](https://www.ncbi.nlm.nih.gov/gene/10207):

> This gene encodes a protein with multiple PDZ domains. PDZ domains mediate protein-protein interactions, and proteins with multiple PDZ domains often organize multimeric complexes at the plasma membrane. This protein localizes to tight junctions and to the apical membrane of epithelial cells. A similar protein in Drosophila is a scaffolding protein which tethers several members of a multimeric signaling complex in photoreceptors. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28881) · Entrez [10207](https://www.ncbi.nlm.nih.gov/gene/10207) · UniProt [Q8NI35](https://www.uniprot.org/uniprotkb/Q8NI35) · Ensembl [ENSG00000132849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132849)

## Data

Gene col 5385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5385); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5385]; `tensor/DDL_lfc|DDL_z.npy` [5385]; `embed/gene_vectors.npy` [5385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5385 or target_col == 5385). Every well: [[PATJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PATJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
