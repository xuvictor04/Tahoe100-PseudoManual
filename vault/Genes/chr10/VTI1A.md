---
symbol: "VTI1A"
type: "gene"
col: 7533
ensembl_id: "ENSG00000151532"
name: "vesicle transport through interaction with t-SNAREs 1A"
location: "10q25.2"
module: 185
arm: "+"
pooled_cpm: 216.16
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# VTI1A

*vesicle transport through interaction with t-SNAREs 1A* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.10× (z +13.9, q 4e-41, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.437× (z -15.1, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.735× (z -8.2, q 2e-14, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS53]] (+0.69, fdr 7e-06), [[EIPR1]] (+0.65, fdr 7e-06), [[COP1]] (+0.64, fdr 7e-06); moves opposite to [[NR1D1]] (-0.60, fdr 1e-05), [[ABCA5]] (-0.60, fdr 1e-05), [[CCDC148]] (-0.56, fdr 1e-05).
> It is in [[Module 185]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +13.9 | 4e-41 | 47/48 (A498, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +11.8 | 8e-30 | 43/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.72×** | +9.3 | 2e-18 | 43/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +9.1 | 9e-18 | 42/48 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.61×** | +8.9 | 8e-17 | 44/48 (LoVo, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +8.7 | 2e-16 | 44/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +8.6 | 5e-16 | 42/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +7.1 | 7e-11 | 38/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.97×** | +6.4 | 1e-08 | 40/45 (A498, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.8 | 3e-07 | 31/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.31×** | +4.9 | 6e-05 | 28/48 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +4.6 | 2e-04 | 22/48 (CFPAC-1, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +4.5 | 4e-04 | 17/48 (LoVo, hTERT-HPNE, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.004 | 32/48 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.012 | 31/49 (RKO, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.023 | 22/48 (A549, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.035 | 27/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.2 | 0.041 | 20/47 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.0 | 0.077 | 21/48 (NCI-H1792, A498, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.082 | 20/48 (NCI-H1792, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.082 | 20/48 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.437×** | -15.1 | 0e+00 | 47/49 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.606×** | -13.3 | 8e-38 | 36/48 (A-172, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -12.9 | 1e-35 | 40/44 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.531×** | -11.4 | 5e-28 | 45/48 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -9.3 | 2e-18 | 43/47 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **0.627×** | -8.8 | 2e-16 | 42/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.735×** | -8.2 | 2e-14 | 41/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.693×** | -6.9 | 4e-10 | 42/49 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.702×** | -6.5 | 6e-09 | 39/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.759×** | -4.8 | 9e-05 | 26/45 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.792×** | -4.3 | 0.001 | 27/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.815×** | -3.9 | 0.005 | 24/48 (SW48, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 280 | 3 (2 ⚠) | 9 (9 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.97× (z +10.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 1.93× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -20.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 222 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -24.2) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.516× (z -8.6) |
| [[LoVo (line)]] | wt | 297 | 5 (2 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.02× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -17.3) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H1573 (line)]] | alt | 266 | 3 (2 ⚠) | 6 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.05× (z +10.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.81× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.651× (z -9.0) |
| [[SW 900 (line)]] | alt | 202 | 7 (3 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.40× (z +10.6) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 2.30× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -13.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 150 | 5 (3 ⚠) | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.58× (z +17.4) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -18.3) ⚠ cell-cycle shift, explains ~68% of this change |
| [[LS 180 (line)]] | wt | 322 | 2 (1 ⚠) | 6 (6 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +9.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.91× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -15.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 184 | 4 (3 ⚠) | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.19× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.358× (z -12.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.473× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 244 | 4 (3 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.23× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -19.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 212 | 4 (1 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.16× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -15.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-427 (line)]] | wt | 354 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -17.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 207 | 5 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -15.3) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HEC-1-A (line)]] | alt | 211 | 1 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 1.81× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -16.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HT-29 (line)]] | alt | 226 | 3 (2 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.84× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -12.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 229 | 3 (2 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.02× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 142 | 2 | 5 (4 ⚠) | [[Auranofin (drug)]] 5 µM 1.88× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.641× (z -9.0) |
| [[HS-578T (line)]] | alt | 155 | 1 | 5 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.08× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -15.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.595× (z -9.1) |
| [[RKO (line)]] | wt | 267 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.18× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.323× (z -14.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.449× (z -10.1) |
| [[SW48 (line)]] | wt | 484 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -15.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 269 | 4 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.49× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -16.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 241 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.21× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -20.1) ⚠ cell-cycle shift, explains ~68% of this change |
| [[CFPAC-1 (line)]] | alt | 148 | 3 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -16.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HOP62 (line)]] | alt | 105 | 3 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -13.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[hTERT-HPNE (line)]] | wt | 215 | 2 (1 ⚠) | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.25× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -17.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H1792 (line)]] | alt | 178 | 2 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -15.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[COLO 205 (line)]] | alt | 255 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 176 | 3 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.52× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 183 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.08× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 231 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.45× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -16.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 215 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.41× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -16.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 176 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -11.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[H4 (line)]] | wt | 180 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.381× (z -8.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 302 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -14.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 257 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 231 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.55× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -34.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 211 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -12.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 263 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.88× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -17.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[C-33 A (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -15.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 160 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 184 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -10.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW 1271 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.226× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change |
| [[AN3 CA (line)]] | alt | 273 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 144 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS53]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 764 |
| [[EIPR1]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[COP1]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[LINC00630]] | +0.64 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[CHCHD3]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 | same gene group |
| [[ULK4]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[INVS]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[EXOC6B]] | +0.62 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[PSMB7]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TALDO1]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[RAB5IF]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[IPO11]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR1D1]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.56 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[BCL3]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 | same gene group |
| [[TAPT1]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[NOTCH2NLA]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ZNF385C]] | -0.53 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[SEPSECS]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[NFKB2]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[RAB30]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[TXNDC16]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[CLK4]] | -0.52 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.1, -13.0); signed map (-15.8, -48.7). **Vector** length 145, 56.1% of its response variance represented; |z| ≥ 3 in 1,440 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +14.8 | +13.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +11.6 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.5 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +11.4 | +9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.1 | +8.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +6.7 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +6.0 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +6.0 | +3.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -15.3 | -8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -13.3 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -13.1 | -13.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -11.6 | -11.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.2 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -6.2 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | vesicle transport through interaction with t-SNAREs 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:112,446,998-112,818,744 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MVti1, Vti1-rp2 |
| Gene groups (HGNC) | SNAREs; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AJ9](https://www.uniprot.org/uniprotkb/Q96AJ9) (Vesicle transport through interaction with t-SNAREs homolog 1A):

> V-SNARE that mediates vesicle transport pathways through interactions with t-SNAREs on the target membrane. These interactions are proposed to mediate aspects of the specificity of vesicle trafficking and to promote fusion of the lipid bilayers. Involved in vesicular transport from the late endosomes to the trans-Golgi network. Along with VAMP7, involved in an non-conventional RAB1-dependent traffic route to the cell surface used by KCNIP1 and KCND2. May be involved in increased cytokine …

**Summary**, from NCBI Gene [143187](https://www.ncbi.nlm.nih.gov/gene/143187):

> The protein encoded by this gene is a member of the family of soluble N-ethylmaleimide-sensitive fusion protein-attachment protein receptors (SNAREs) that function in intracellular trafficking. This family member is involved in vesicular transport between endosomes and the trans-Golgi network. It is a vesicle-associated SNARE (v-SNARE) that interacts with target membrane SNAREs (t-SNAREs). Polymorphisms in this gene have been associated with binocular function, and also with susceptibility to …

**Accessions** — [HGNC:17792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17792) · Entrez [143187](https://www.ncbi.nlm.nih.gov/gene/143187) · UniProt [Q96AJ9](https://www.uniprot.org/uniprotkb/Q96AJ9) · Ensembl [ENSG00000151532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151532)

## Data

Gene col 7533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7533); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7533]; `tensor/DDL_lfc|DDL_z.npy` [7533]; `embed/gene_vectors.npy` [7533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7533 or target_col == 7533). Every well: [[VTI1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VTI1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
