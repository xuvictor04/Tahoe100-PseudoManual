---
symbol: "NUMB"
type: "gene"
col: 5490
ensembl_id: "ENSG00000133961"
name: "NUMB endocytic adaptor protein"
location: "14q24.3"
module: 1
arm: "-"
pooled_cpm: 253.69
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NUMB

*NUMB endocytic adaptor protein* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +9.3, q 7e-18, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.457× (z -18.3, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.717× (z -7.7, q 9e-13, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYNJ1]] (+0.60, fdr 3e-05), [[TMEM50A]] (+0.60, fdr 1e-05), [[PDE6D]] (+0.58, fdr 7e-05); moves opposite to [[ZC3HAV1L]] (-0.56, fdr 1e-04), [[RABGGTB]] (-0.55, fdr 1e-05), [[ZZZ3]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMEM158]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +9.3 | 7e-18 | 40/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.7 | 6e-09 | 33/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +6.6 | 7e-09 | 30/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +5.8 | 1e-06 | 26/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.20×** | +4.2 | 0.004 | 24/47 (H4, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.13 | 22/48 (PANC-1, HEC-1-A, …) | top dose only | composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | 1.37× | +3.2 | 0.13 | 20/48 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.16 | 16/47 (NCI-H2030, HOP62, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.457×** | -18.3 | 0e+00 | 46/49 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.452×** | -17.8 | 0e+00 | 41/44 (SK-MEL-2, SW 900, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.453×** | -17.1 | 0e+00 | 43/45 (HS-578T, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.634×** | -10.2 | 2e-22 | 42/47 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.708×** | -8.0 | 1e-13 | 34/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -7.7 | 9e-13 | 38/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.733×** | -7.2 | 4e-11 | 38/48 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.746×** | -6.8 | 5e-10 | 32/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.771×** | -6.1 | 8e-08 | 30/48 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.810×** | -4.9 | 5e-05 | 24/48 (HS-578T, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.810×** | -4.9 | 5e-05 | 25/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.635×** | -4.6 | 2e-04 | 28/48 (NCI-H460, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.874× | -4.4 | 4e-04 | 6/48 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.676×** | -3.9 | 0.003 | 27/48 (AsPC-1, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -3.9 | 0.004 | 18/48 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.687×** | -3.8 | 0.005 | 27/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.721×** | -3.3 | 0.032 | 22/48 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.871× | -3.2 | 0.039 | 14/48 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.869× | -3.1 | 0.046 | 14/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.739×** | -3.0 | 0.062 | 19/48 (CFPAC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.883× | -2.9 | 0.089 | 18/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 324 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -19.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 552 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.465× (z -10.2) |
| [[A-172 (line)]] | wt | 300 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -13.1) |
| [[BT-474 (line)]] | alt | 217 | 5 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -12.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 291 | 3 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 260 | 3 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.80× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.590× (z -8.5) |
| [[HOP62 (line)]] | alt | 417 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -14.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 193 | 1 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.422× (z -13.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.555× (z -9.3) |
| [[A549 (line)]] | wt | 322 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -22.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 405 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -9.8) |
| [[PANC-1 (line)]] | alt | 148 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +18.8) | — |
| [[HepG2_C3A (line)]] | wt | 249 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 388 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 318 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 236 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.528× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 261 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -13.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 203 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -15.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 296 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -17.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 149 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -11.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 363 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 381 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -14.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 315 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -16.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 316 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -11.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 352 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -19.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 199 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -15.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 156 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -11.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 200 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.476× (z -10.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.547× (z -9.1) |
| [[LoVo (line)]] | wt | 148 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 206 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.476× (z -11.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 176 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -13.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 198 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -22.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 216 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.505× (z -9.4) |
| [[C32 (line)]] | wt | 229 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -14.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 188 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 228 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 229 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 144 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.36× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 161 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 268 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 238 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -13.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 197 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 222 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 229 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNJ1]] | +0.60 | +0.54 / +0.43 | both halves | 3e-05 | STRING 582 |
| [[TMEM50A]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PDE6D]] | +0.58 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[WDR44]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[OST4]] | +0.54 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[STX12]] | +0.54 | +0.37 / +0.45 | both halves | 9e-05 |  |
| [[POLD4]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[TIMP1]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[BTRC]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 | pathway: Degradation of GLI1 by the proteasome; STRING 438 |
| [[HOOK3]] | +0.53 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[MPC2]] | +0.53 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[MORC3]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3HAV1L]] | -0.56 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[RABGGTB]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ZZZ3]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TCERG1]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[DUXAP8]] | -0.54 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[MRPL3]] | -0.53 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[DUS3L]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZNF485]] | -0.53 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[TGFBRAP1]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ATIC]] | -0.52 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[BYSL]] | -0.52 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[PFAS]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM158]] | B | TMEM158 activity raises NUMB's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without TMEM158 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[S100A6]] | B | S100A6 activity raises NUMB's level | lines that do not express S100A6 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without S100A6 | 0.089 | ⚠ within organs, on part of the lines; also absent: GPRC5D-AS1, HLA-H, PRRG1; maybe low, not absent; its own permutation p |
| [[TIMP1]] | C | TIMP1 activity raises NUMB's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 1.45× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.9, -39.5); signed map (-16.6, 15.4). **Vector** length 105, 38.8% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.9 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | -0.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -7.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.1 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | NUMB endocytic adaptor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,275,107-73,458,617 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf41 |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 11 pathways, smallest: Activated NOTCH1 Transmits Signal to the Nucleus; Recycling pathway of L1; Degradation of GLI1 by the proteasome |
| Matched by | ensembl_id |

**Function**, from UniProt [P49757](https://www.uniprot.org/uniprotkb/P49757) (Protein numb homolog):

> Regulates clathrin-mediated receptor endocytosis. Plays a role in the process of neurogenesis (By similarity). Required throughout embryonic neurogenesis to maintain neural progenitor cells, also called radial glial cells (RGCs), by allowing their daughter cells to choose progenitor over neuronal cell fate (By similarity). Not required for the proliferation of neural progenitor cells before the onset of neurogenesis. Also involved postnatally in the subventricular zone (SVZ) neurogenesis by …

**Summary**, from NCBI Gene [8650](https://www.ncbi.nlm.nih.gov/gene/8650):

> The protein encoded by this gene plays a role in the determination of cell fates during development. The encoded protein, whose degradation is induced in a proteasome-dependent manner by MDM2, is a membrane-bound protein that has been shown to associate with EPS15, LNX1, and NOTCH1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:8060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8060) · Entrez [8650](https://www.ncbi.nlm.nih.gov/gene/8650) · UniProt [P49757](https://www.uniprot.org/uniprotkb/P49757) · Ensembl [ENSG00000133961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133961)

## Data

Gene col 5490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5490); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5490]; `tensor/DDL_lfc|DDL_z.npy` [5490]; `embed/gene_vectors.npy` [5490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5490 or target_col == 5490). Every well: [[NUMB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUMB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
