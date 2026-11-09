---
symbol: "TNRC6C"
type: "gene"
col: 1229
ensembl_id: "ENSG00000078687"
name: "trinucleotide repeat containing adaptor 6C"
location: "17q25.3"
module: 25
arm: "-"
pooled_cpm: 102.66
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TNRC6C

*trinucleotide repeat containing adaptor 6C* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +34.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.442× (z -20.7, q 0e+00, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.656× (z -10.7, q 1e-24, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRCH3]] (+0.69, fdr 7e-06), [[TERF2IP]] (+0.67, fdr 7e-06), [[EIF1B]] (+0.66, fdr 7e-06); moves opposite to [[GPN1]] (-0.73, fdr 7e-06), [[CCT3]] (-0.72, fdr 7e-06), [[TCP1]] (-0.72, fdr 7e-06).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[YY1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +34.2 | 0e+00 | 47/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +19.3 | 0e+00 | 39/49 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +16.4 | 0e+00 | 42/48 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +12.6 | 3e-34 | 39/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +10.3 | 6e-23 | 39/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +9.5 | 2e-19 | 36/48 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +8.4 | 5e-15 | 31/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +8.0 | 9e-14 | 30/48 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +7.6 | 2e-12 | 31/48 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +7.2 | 3e-11 | 29/48 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +6.0 | 9e-08 | 29/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 2e-07 | 25/48 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.3 | 6e-06 | 26/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.8 | 8e-05 | 19/48 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 22/49 (BT-474, NCI-H2030, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.40×** | +4.5 | 3e-04 | 22/48 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.442×** | -20.7 | 0e+00 | 39/49 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.478×** | -17.3 | 0e+00 | 39/45 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -16.6 | 0e+00 | 34/44 (SK-MEL-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.378×** | -12.9 | 6e-36 | 40/45 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.656×** | -10.7 | 1e-24 | 37/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -9.7 | 3e-20 | 38/48 (SW 900, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -8.4 | 3e-15 | 32/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -8.4 | 5e-15 | 33/48 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.759×** | -6.7 | 1e-09 | 27/47 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.713×** | -4.5 | 4e-04 | 21/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.720×** | -4.4 | 7e-04 | 21/48 (SW 900, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.844× | -4.3 | 9e-04 | 20/48 (C-33 A, BT-474, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.735×** | -4.1 | 0.002 | 22/48 (SW 900, A549, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.003 | 18/48 (SW 900, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.849× | -4.0 | 0.003 | 10/49 (A498, BT-474, …) | top dose only | plate-row cell shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.744×** | -3.9 | 0.003 | 22/48 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.920× | -3.0 | 0.086 | 1/48 (MIA PaCa-2) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.2 | 8 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +29.9) | [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 167 | 3 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.610× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 133 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +21.0) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.414× (z -10.4) |
| [[A498 (line)]] | wt | 90.2 | 5 (1 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 125 | 5 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.482× (z -8.9) |
| [[SNU-423 (line)]] | alt | 106 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -13.6) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.445× (z -9.7) |
| [[SW 900 (line)]] | alt | 206 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.374× (z -11.9) |
| [[KATO III (line)]] | alt | 156 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -20.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 175 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +22.6) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -27.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.610× (z -9.5) |
| [[HT-29 (line)]] | alt | 108 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.375× (z -12.5) |
| [[RKO (line)]] | wt | 96.8 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +16.7) | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -17.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 142 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.0929× (z -31.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 150 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.435× (z -9.2) |
| [[A-427 (line)]] | wt | 146 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -20.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 66.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.9) | — |
| [[COLO 205 (line)]] | alt | 135 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 73.7 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.467× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 103 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 106 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +17.7) | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 70.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 79.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +21.5) | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 96.4 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.427× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 86.2 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.5) |
| [[A549 (line)]] | wt | 75.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 51.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +17.2) | — |
| [[SHP-77 (line)]] | alt | 245 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -13.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 214 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 128 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -16.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 112 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 74.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -19.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 107 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 36.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +21.6) | — |
| [[SW1417 (line)]] | alt | 74.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 80.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.4) | — |
| [[C32 (line)]] | wt | 84.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.6) | — |
| [[HCT15 (line)]] | alt | 136 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -18.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 36.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 82.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +15.9) | — |
| [[SNU-1 (line)]] | wt | 82.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -13.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +16.4) | — |
| [[NCI-H2030 (line)]] | alt | 56.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +19.8) | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRCH3]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[EIF1B]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[HIC2]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[SHOC2]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[ACAP1]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[NBPF19]] | +0.61 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[ERF]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[ZBTB7A]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | +0.60 | +0.52 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FAM193A]] | +0.60 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPN1]] | -0.73 | -0.72 / -0.70 | both halves | 7e-06 |  |
| [[CCT3]] | -0.72 | -0.72 / -0.62 | both halves | 7e-06 | pathway: Cilium Assembly |
| [[TCP1]] | -0.72 | -0.72 / -0.62 | both halves | 7e-06 | pathway: Cilium Assembly |
| [[CCT5]] | -0.69 | -0.68 / -0.63 | both halves | 7e-06 | pathway: Cilium Assembly |
| [[RPE]] | -0.69 | -0.67 / -0.68 | both halves | 7e-06 |  |
| [[UBQLN1]] | -0.69 | -0.72 / -0.67 | both halves | 7e-06 |  |
| [[OPA1]] | -0.68 | -0.71 / -0.66 | both halves | 7e-06 |  |
| [[CCT2]] | -0.68 | -0.58 / -0.66 | both halves | 8e-06 | pathway: Cilium Assembly |
| [[USP14]] | -0.68 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[AHSA1]] | -0.68 | -0.74 / -0.64 | both halves | 7e-06 |  |
| [[GSR]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 | pathway: TP53 Regulates Metabolic Genes |
| [[DLAT]] | -0.66 | -0.64 / -0.58 | both halves | 7e-06 | pathway: Signaling by Nuclear Receptors |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YY1]] | C | YY1's natural level weakens TNRC6C's drug response | YY1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.17; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.9, -14.2); signed map (-7.0, 5.7). **Vector** length 123, 37.5% of its response variance represented; |z| ≥ 3 in 1,377 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +34.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.6 | +12.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.5 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +16.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.3 | +3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.1 | +1.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -9.6 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.7 | -9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -8.4 | -8.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -6.9 | -12.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -4.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | trinucleotide repeat containing adaptor 6C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:77,958,703-78,108,822 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1582, FLJ20015 |
| Gene groups (HGNC) | TNRC6 adaptor family |
| Reactome | 67 pathways, smallest: Post-transcriptional silencing by small RNAs; Regulation of NPAS4 mRNA translation; Regulation of CDH11 mRNA translation by microRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCJ0](https://www.uniprot.org/uniprotkb/Q9HCJ0) (Trinucleotide repeat-containing gene 6C protein):

> Plays a role in RNA-mediated gene silencing by micro-RNAs (miRNAs). Required for miRNA-dependent translational repression of complementary mRNAs by argonaute family proteins. As scaffoldng protein associates with argonaute proteins bound to partially complementary mRNAs and simultaneously can recruit CCR4-NOT and PAN deadenylase complexes.

**Summary**, from NCBI Gene [57690](https://www.ncbi.nlm.nih.gov/gene/57690):

> Predicted to enable RNA binding activity. Involved in miRNA-mediated post-transcriptional gene silencing; positive regulation of nuclear-transcribed mRNA catabolic process, deadenylation-dependent decay; and positive regulation of nuclear-transcribed mRNA poly(A) tail shortening. Predicted to be located in cytosol. Predicted to be active in P-body and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29318) · Entrez [57690](https://www.ncbi.nlm.nih.gov/gene/57690) · UniProt [Q9HCJ0](https://www.uniprot.org/uniprotkb/Q9HCJ0) · Ensembl [ENSG00000078687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078687)

## Data

Gene col 1229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1229); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1229]; `tensor/DDL_lfc|DDL_z.npy` [1229]; `embed/gene_vectors.npy` [1229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1229 or target_col == 1229). Every well: [[TNRC6C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNRC6C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
