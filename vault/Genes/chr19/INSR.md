---
symbol: "INSR"
type: "gene"
col: 10051
ensembl_id: "ENSG00000171105"
name: "insulin receptor"
location: "19p13.2"
module: 69
arm: "+"
pooled_cpm: 86.8
n_lines_expressing: 47
n_dd_up: 13
n_dd_down: 39
n_dd_up_clean: 10
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# INSR

*insulin receptor* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Rapamycin (drug)]] 5 µM: 1.22× (z +5.3, q 6e-05, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.417× (z -22.9, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.65, fdr 1e-05), [[REPS2]] (+0.65, fdr 1e-05), [[RB1CC1]] (+0.63, fdr 2e-05); moves opposite to [[PUS7L]] (-0.53, fdr 2e-05), [[PPIL1]] (-0.50, fdr 2e-05), [[TAS2R30]] (-0.48, fdr 9e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 5 µM |  | **1.22×** | +5.3 | 6e-05 | 28/45 (C-33 A, A-172, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 2e-04 | 27/45 (LoVo, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 1e-03 | 27/46 (BT-474, NCI-H2347, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.59×** | +4.5 | 0.001 | 27/47 (LoVo, HT-29, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.16× | +3.9 | 0.010 | 11/46 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.8 | 0.010 | 17/45 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.010 | 22/46 (LoVo, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[MK-3903 (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.011 | 20/45 (LoVo, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.015 | 20/46 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +3.6 | 0.015 | 21/44 (NCI-H23, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.015 | 21/45 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.027 | 16/45 (LoVo, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.20× | +3.3 | 0.038 | 16/45 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.042 | 19/45 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.20×** | +3.3 | 0.042 | 21/45 (LoVo, BT-474, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.042 | 17/46 (BT-474, Hs 766T, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.043 | 15/45 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.417×** | -22.9 | 0e+00 | 43/45 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.277×** | -22.9 | 0e+00 | 43/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.296×** | -22.6 | 0e+00 | 43/45 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.328×** | -20.6 | 0e+00 | 44/45 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.433×** | -15.5 | 0e+00 | 41/45 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.448×** | -14.9 | 0e+00 | 43/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.222×** | -14.6 | 0e+00 | 46/46 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -13.5 | 8e-40 | 41/45 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.535×** | -11.6 | 3e-29 | 36/45 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.536×** | -11.5 | 5e-29 | 39/45 (SNU-423, LS 180, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.313×** | -11.3 | 1e-27 | 42/45 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.326×** | -10.9 | 9e-26 | 44/45 (HT-29, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.544×** | -10.8 | 1e-25 | 38/44 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.360×** | -9.9 | 2e-21 | 38/45 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.588×** | -9.8 | 3e-21 | 35/45 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.378×** | -9.4 | 2e-19 | 40/45 (MIA PaCa-2, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -9.1 | 3e-18 | 37/45 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.406×** | -8.7 | 9e-17 | 38/45 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.526×** | -8.5 | 6e-16 | 42/45 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.672×** | -7.3 | 5e-12 | 30/45 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 159 | 0 | 25 (12 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.152× (z -25.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -22.8) |
| [[SNU-423 (line)]] | alt | 220 | 0 | 24 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -32.2) |
| [[LS 180 (line)]] | wt | 175 | 0 | 15 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -18.8) |
| [[A-172 (line)]] | wt | 119 | 0 | 14 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.261× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 97.1 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -20.7) |
| [[SW480 (line)]] | alt | 84.8 | 0 | 14 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.139× (z -22.9) |
| [[COLO 205 (line)]] | alt | 133 | 0 | 13 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.203× (z -15.1) |
| [[HOP62 (line)]] | alt | 58.6 | 1 (1 ⚠) | 11 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.26× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 81.4 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -31.2) |
| [[SNU-1 (line)]] | wt | 97.2 | 0 | 12 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.197× (z -14.0) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.213× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 112 | 0 | 11 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -15.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -13.9) |
| [[HCT15 (line)]] | alt | 170 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -20.1) |
| [[SW48 (line)]] | wt | 118 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0533× (z -26.4) |
| [[BT-474 (line)]] | alt | 256 | 0 | 10 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.166× (z -14.3) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -12.0) |
| [[HT-29 (line)]] | alt | 102 | 0 | 10 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.222× (z -16.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 82.7 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.0) |
| [[LoVo (line)]] | wt | 140 | 1 (1 ⚠) | 9 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.283× (z -17.5) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.306× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 130 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -16.6) |
| [[SW 900 (line)]] | alt | 98.3 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.5) |
| [[A498 (line)]] | wt | 54.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -18.4) |
| [[CFPAC-1 (line)]] | alt | 53.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -13.4) |
| [[Hs 766T (line)]] | wt | 56.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -13.7) |
| [[RKO (line)]] | wt | 94.2 | 1 (1 ⚠) | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.307× (z -17.0) |
| [[A-427 (line)]] | wt | 127 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0992× (z -26.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.276× (z -21.8) |
| [[HEC-1-A (line)]] | alt | 46.5 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.214× (z -14.1) |
| [[KATO III (line)]] | alt | 131 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 33.7 | 1 (1 ⚠) | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Harringtonine (drug)]] 0.5 µM 0.204× (z -14.2) |
| [[PANC-1 (line)]] | alt | 23.0 | 3 (2 ⚠) | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.48× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -10.1) |
| [[SW1417 (line)]] | alt | 99.9 | 0 | 6 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.233× (z -16.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.496× (z -11.0) |
| [[A549 (line)]] | wt | 61.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -19.5) |
| [[H4 (line)]] | wt | 89.3 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.168× (z -14.4) |
| [[C32 (line)]] | wt | 71.5 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.343× (z -10.0) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.344× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 66.8 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -11.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.9) |
| [[C-33 A (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 82.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.304× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 30.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 9.74× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.222× (z -8.5) |
| [[AN3 CA (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[CHP-212 (line)]] | wt | 93.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 242 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -9.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 86.7 | 0 | 1 | — | [[Daidzin (drug)]] 5 µM 0.0643× (z -9.2) |
| [[SW 1271 (line)]] | alt | 112 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0498× (z -14.8) |
| [[HS-578T (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[REPS2]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[RB1CC1]] | +0.63 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[YPEL3]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[HECA]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.62 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[UBXN7]] | +0.60 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[HDAC5]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[RALBP1]] | +0.58 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[AKAP13-AS1]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[MOB2]] | +0.57 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[CDKN1C]] | +0.56 | +0.40 / +0.62 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS7L]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PPIL1]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TAS2R30]] | -0.48 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[PDAP1]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[DNAJC10]] | -0.47 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[EIF5A]] | -0.47 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[EMC1]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers INSR's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[BEX4]] | B | BEX4 activity lowers INSR's level | lines that do not express BEX4 (22) vs lines expressing it (28) | 1.80× higher at baseline in the lines without BEX4 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, ZNF229, BEX2 |
| [[YPEL2]] | C | YPEL2 activity raises INSR's level | lines that do not express YPEL2 (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without YPEL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAGI1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.3, -45.2); signed map (-17.5, 10.9). **Vector** length 106, 35.6% of its response variance represented; |z| ≥ 3 in 1,767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Rapamycin (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.5 | +3.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +3.3 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | -0.6 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +3.2 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.2 | -20.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.8 | -10.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.9 | -9.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.6 | -8.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.4 | -11.3 |
|  | [[EX229 (drug)]] 5 µM |  | -6.1 | -9.9 |

## What is on record

|  |  |
|---|---|
| Name | insulin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,112,255-7,294,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD220 |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; Insulin receptor family |
| Reactome | 10 pathways, smallest: IRS activation; Signal attenuation; Insulin receptor recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [P06213](https://www.uniprot.org/uniprotkb/P06213) (Insulin receptor):

> Receptor tyrosine kinase which mediates the pleiotropic actions of insulin. Binding of insulin leads to phosphorylation of several intracellular substrates, including, insulin receptor substrates (IRS1, 2, 3, 4), SHC, GAB1, CBL and other signaling intermediates. Each of these phosphorylated proteins serve as docking proteins for other signaling proteins that contain Src-homology-2 domains (SH2 domain) that specifically recognize different phosphotyrosine residues, including the p85 regulatory …

**Summary**, from NCBI Gene [3643](https://www.ncbi.nlm.nih.gov/gene/3643):

> This gene encodes a member of the receptor tyrosine kinase family of proteins. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form a heterotetrameric receptor. Binding of insulin or other ligands to this receptor activates the insulin signaling pathway, which regulates glucose uptake and release, as well as the synthesis and storage of carbohydrates, lipids and protein. Mutations in this gene underlie the inherited severe insulin resistance …

**Accessions** — [HGNC:6091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6091) · Entrez [3643](https://www.ncbi.nlm.nih.gov/gene/3643) · UniProt [P06213](https://www.uniprot.org/uniprotkb/P06213) · Ensembl [ENSG00000171105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171105)

## Data

Gene col 10051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10051); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10051]; `tensor/DDL_lfc|DDL_z.npy` [10051]; `embed/gene_vectors.npy` [10051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10051 or target_col == 10051). Every well: [[INSR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INSR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
