---
symbol: "FBXL17"
type: "gene"
col: 7023
ensembl_id: "ENSG00000145743"
name: "F-box and leucine rich repeat protein 17"
location: "5q21.3"
module: 137
arm: "+"
pooled_cpm: 191.49
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 34
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# FBXL17

*F-box and leucine rich repeat protein 17* — 5q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.47× (z +5.0, q 4e-04, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (19 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.301× (z -16.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID1B]] (+0.76, fdr 7e-06), [[TCF12]] (+0.72, fdr 7e-06), [[PARD3B]] (+0.69, fdr 1e-05); moves opposite to [[GIPR]] (-0.63, fdr 3e-05), [[FCHSD1]] (-0.63, fdr 1e-05), [[F11R]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ITPR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +5.0 | 4e-04 | 35/47 (LoVo, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.075 | 29/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.075 | 37/48 (CFPAC-1, SW48, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.20 | 26/47 (A-172, C32, …) | inconsistent across doses |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.20 | 30/48 (SNU-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.20 | 27/49 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.20 | 29/48 (Hs 766T, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.301×** | -16.0 | 0e+00 | 47/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.303×** | -15.9 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.344×** | -14.2 | 2e-43 | 47/48 (SW480, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.456×** | -10.4 | 3e-23 | 47/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.449×** | -10.2 | 1e-22 | 45/47 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.463×** | -10.2 | 1e-22 | 42/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.525×** | -8.5 | 1e-15 | 46/48 (HT-29, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.636×** | -8.5 | 2e-15 | 36/48 (LOX-IMVI, C32, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.545×** | -8.0 | 5e-14 | 41/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.554×** | -7.8 | 3e-13 | 42/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.574×** | -7.4 | 1e-11 | 43/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.600×** | -6.8 | 6e-10 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.402×** | -6.3 | 1e-08 | 45/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.613×** | -6.2 | 2e-08 | 37/44 (NCI-H23, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.545×** | -6.2 | 2e-08 | 36/49 (H4, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -5.2 | 5e-06 | 39/48 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.691×** | -4.9 | 3e-05 | 32/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -3.9 | 0.002 | 28/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.695×** | -3.7 | 0.005 | 31/48 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.746×** | -3.7 | 0.005 | 30/48 (SW 900, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.012 | 27/49 (HT-29, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.615×** | -3.4 | 0.015 | 27/48 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.638×** | -3.1 | 0.036 | 24/48 (SHP-77, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -3.1 | 0.036 | 27/48 (C32, SW480, …) | top dose only | plate-row cell shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.648×** | -3.0 | 0.048 | 26/48 (LoVo, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.731×** | -3.0 | 0.054 | 26/48 (LoVo, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 207 | 0 | 17 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.285× (z -13.1) |
| [[HT-29 (line)]] | alt | 223 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.204× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 247 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.7) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -16.2) |
| [[PANC-1 (line)]] | alt | 256 | 0 | 13 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -17.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -13.9) |
| [[SW480 (line)]] | alt | 191 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -20.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.183× (z -19.8) |
| [[LoVo (line)]] | wt | 227 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -21.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -16.4) |
| [[SNU-1 (line)]] | wt | 207 | 0 | 10 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.138× (z -17.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.302× (z -11.2) |
| [[C32 (line)]] | wt | 286 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -19.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -14.8) |
| [[HCT15 (line)]] | alt | 194 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -14.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.240× (z -13.6) |
| [[J82 (line)]] | alt | 155 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -12.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.290× (z -12.0) |
| [[KATO III (line)]] | alt | 112 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -15.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.281× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 170 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -16.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.301× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 247 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.366× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 150 | 1 (1 ⚠) | 7 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.325× (z -11.2) |
| [[A-427 (line)]] | wt | 226 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -12.4) |
| [[LS 180 (line)]] | wt | 256 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -18.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.200× (z -17.5) |
| [[COLO 205 (line)]] | alt | 219 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -18.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.200× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 173 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -14.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.219× (z -13.6) |
| [[A498 (line)]] | wt | 244 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -13.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -9.7) |
| [[AN3 CA (line)]] | alt | 294 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.242× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 141 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -14.9) |
| [[C-33 A (line)]] | alt | 240 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.296× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 247 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -19.8) |
| [[SK-MEL-2 (line)]] | alt | 339 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.249× (z -14.4) |
| [[SW 900 (line)]] | alt | 148 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -13.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.378× (z -9.5) |
| [[SW1417 (line)]] | alt | 109 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -12.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.313× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 197 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -14.7) |
| [[HS-578T (line)]] | alt | 168 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 180 | 1 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.87× (z +10.1) ⚠ cell-cycle shift, explains ~73% of this change | [[Panobinostat (drug)]] 5 µM 0.353× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 153 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -16.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.231× (z -14.3) |
| [[A549 (line)]] | wt | 116 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.283× (z -10.1) |
| [[HOP62 (line)]] | alt | 216 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 217 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -13.8) |
| [[SHP-77 (line)]] | alt | 241 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.312× (z -12.8) |
| [[SNU-423 (line)]] | alt | 140 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.395× (z -9.0) |
| [[SW48 (line)]] | wt | 220 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -11.5) |
| [[A-172 (line)]] | wt | 209 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -17.2) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -9.4) |
| [[BT-474 (line)]] | alt | 66.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 82.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 254 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[Hs 766T (line)]] | wt | 94.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -9.1) |
| [[SW 1271 (line)]] | alt | 317 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -10.2) |
| [[CHP-212 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID1B]] | +0.76 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[TCF12]] | +0.72 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PARD3B]] | +0.69 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | +0.65 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[ARID2]] | +0.64 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[SLC12A2-DT]] | +0.63 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[TBC1D5]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[UFL1-AS1]] | +0.62 | +0.60 / +0.31 | both halves | 2e-04 |  |
| [[ATXN7]] | +0.62 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[TULP4]] | +0.61 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[UBTF]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[ASXL2]] | +0.61 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIPR]] | -0.63 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[FCHSD1]] | -0.63 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[F11R]] | -0.61 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MAST3]] | -0.58 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SLC8B1]] | -0.57 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[BAIAP3]] | -0.57 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ARPC1A]] | -0.57 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ATG16L2]] | -0.56 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[AHDC1]] | -0.56 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PLD3]] | -0.56 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[LMTK3]] | -0.56 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[TCIRG1]] | -0.55 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR2]] | B | ITPR2 activity raises FBXL17's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without ITPR2 | 0.091 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-3.8, 7.5); signed map (23.9, -32.0). **Vector** length 103, 43.6% of its response variance represented; |z| ≥ 3 in 1,441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~79% of this change | +5.9 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.9 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | -16.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.0 | -14.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.4 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.3 — chr5:107,859,035-108,382,098 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434C1715, Fbx13, Fbl17; previously FBXO13 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 5 pathways, smallest: Regulation of BACH1 activity; KEAP1-NFE2L2 pathway; Cellular response to chemical stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UF56](https://www.uniprot.org/uniprotkb/Q9UF56) (F-box/LRR-repeat protein 17):

> Substrate-recognition component of the SCF(FBXL17) E3 ubiquitin ligase complex, a key component of a quality control pathway required to ensure functional dimerization of BTB domain-containing proteins (dimerization quality control, DQC). FBXL17 specifically recognizes and binds a conserved degron of non-consecutive residues present at the interface of BTB dimers of aberrant composition: aberrant BTB dimer are then ubiquitinated by the SCF(FBXL17) complex and degraded by the proteasome. The …

**Summary**, from NCBI Gene [64839](https://www.ncbi.nlm.nih.gov/gene/64839):

> Members of the F-box protein family, such as FBXL17, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13615) · Entrez [64839](https://www.ncbi.nlm.nih.gov/gene/64839) · UniProt [Q9UF56](https://www.uniprot.org/uniprotkb/Q9UF56) · Ensembl [ENSG00000145743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145743)

## Data

Gene col 7023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7023); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7023]; `tensor/DDL_lfc|DDL_z.npy` [7023]; `embed/gene_vectors.npy` [7023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7023 or target_col == 7023). Every well: [[FBXL17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
