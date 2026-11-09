---
symbol: "UBE2E2"
type: "gene"
col: 11264
ensembl_id: "ENSG00000182247"
name: "ubiquitin conjugating enzyme E2 E2"
location: "3p24.3"
module: 113
arm: "+"
pooled_cpm: 353.1
n_lines_expressing: 39
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 19
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# UBE2E2

*ubiquitin conjugating enzyme E2 E2* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.68× (z +12.4, q 2e-32, up in 30 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.361× (z -35.7, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABGAP1L]] (+0.66, fdr 1e-05), [[LDLRAD3]] (+0.62, fdr 1e-05), [[TANC2]] (+0.61, fdr 1e-05); moves opposite to [[HOXA3]] (-0.58, fdr 2e-05), [[GLE1]] (-0.58, fdr 1e-05), [[IKZF4]] (-0.53, fdr 3e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[RBMS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +12.4 | 2e-32 | 30/37 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +11.9 | 3e-30 | 33/37 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +10.5 | 1e-23 | 36/38 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +10.5 | 1e-23 | 21/37 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +10.2 | 4e-22 | 34/37 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +10.1 | 6e-22 | 30/37 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +9.1 | 1e-17 | 30/37 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +8.5 | 2e-15 | 31/37 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +8.4 | 2e-15 | 27/37 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +7.3 | 1e-11 | 30/37 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +7.2 | 3e-11 | 28/37 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +6.8 | 7e-10 | 30/37 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +6.3 | 2e-08 | 22/37 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.7 | 5e-07 | 27/35 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +5.5 | 1e-06 | 22/37 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +4.4 | 4e-04 | 22/37 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.4 | 4e-04 | 9/38 (CFPAC-1, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +4.3 | 4e-04 | 16/37 (SW480, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.361×** | -35.7 | 0e+00 | 37/38 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.406×** | -22.3 | 0e+00 | 36/38 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.394×** | -22.2 | 0e+00 | 33/35 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.530×** | -15.1 | 0e+00 | 34/36 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -14.2 | 2e-43 | 35/37 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -13.6 | 7e-40 | 35/39 (LOX-IMVI, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.686×** | -9.3 | 9e-19 | 36/37 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.774×** | -9.0 | 2e-17 | 24/37 (HOP62, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.693×** | -8.4 | 3e-15 | 22/35 (NCI-H2347, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.746×** | -7.3 | 2e-11 | 25/37 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.794×** | -5.7 | 5e-07 | 21/37 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.851× | -5.7 | 7e-07 | 12/37 (LOX-IMVI, SW1417, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.694×** | -4.7 | 1e-04 | 25/36 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.831×** | -4.6 | 2e-04 | 19/38 (HOP62, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.838× | -4.4 | 4e-04 | 18/37 (SW 900, SNU-423, …) | all doses, stronger at high dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.855× | -3.8 | 0.006 | 11/38 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.911× | -3.3 | 0.031 | 3/38 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.911× | -3.3 | 0.031 | 7/37 (LoVo, SW 900, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.879× | -3.2 | 0.039 | 6/37 (SW 900, SNU-423, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 0.916× | -2.9 | 0.095 | 2/38 (NCI-H2347, BT-474) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 199 | 19 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 269 | 12 (6 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 0.05 µM 2.06× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.05× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -21.5) |
| [[NCI-H2347 (line)]] | alt | 537 | 6 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -34.6) |
| [[SW 900 (line)]] | alt | 284 | 8 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -25.4) |
| [[SW480 (line)]] | alt | 259 | 8 (2 ⚠) | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.86× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -21.3) |
| [[BT-474 (line)]] | alt | 429 | 9 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.64× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -20.9) |
| [[PANC-1 (line)]] | alt | 404 | 9 (2 ⚠) | 5 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.61× (z +20.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -29.3) |
| [[AsPC-1 (line)]] | alt | 340 | 9 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +23.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -29.6) |
| [[HOP62 (line)]] | alt | 651 | 3 | 10 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 2.11× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -31.9) |
| [[Panc 03.27 (line)]] | alt | 479 | 5 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -29.0) |
| [[SW1417 (line)]] | alt | 519 | 1 | 11 (6 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 1.67× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -29.9) |
| [[A-172 (line)]] | wt | 218 | 4 | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -21.3) |
| [[J82 (line)]] | alt | 519 | 3 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +18.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -35.5) |
| [[HS-578T (line)]] | alt | 517 | 5 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -32.1) |
| [[SNU-423 (line)]] | alt | 594 | 3 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -29.0) |
| [[A498 (line)]] | wt | 248 | 4 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -23.1) |
| [[HEC-1-A (line)]] | alt | 1,076 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -33.9) |
| [[NCI-H1573 (line)]] | alt | 336 | 5 (1 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.92× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 569 | 3 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.96× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -18.3) |
| [[HT-29 (line)]] | alt | 191 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 564 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -37.1) |
| [[A549 (line)]] | wt | 518 | 2 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.18× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -31.0) |
| [[NCI-H2030 (line)]] | alt | 140 | 6 (3 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 2.35× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 168 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 433 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -21.2) |
| [[NCI-H1792 (line)]] | alt | 544 | 2 (1 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.95× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -28.1) |
| [[C-33 A (line)]] | alt | 490 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -20.5) |
| [[HCT15 (line)]] | alt | 541 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -21.0) |
| [[NCI-H23 (line)]] | alt | 379 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -23.9) |
| [[SK-MEL-2 (line)]] | alt | 598 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -20.2) |
| [[H4 (line)]] | wt | 176 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 90.7 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.28× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.282× (z -11.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -8.8) |
| [[LoVo (line)]] | wt | 416 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -30.7) |
| [[SW 1271 (line)]] | alt | 566 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.5) |
| [[A-427 (line)]] | wt | 467 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.8) |
| [[CHP-212 (line)]] | wt | 357 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -30.1) |
| [[NCI-H596 (line)]] | alt | 346 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.323× (z -11.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 56.4 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 66.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 52.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 25.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 27.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 33.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGAP1L]] | +0.66 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LDLRAD3]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TANC2]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PALM2AKAP2]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MT1A]] | +0.56 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[TMEM241]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[DUSP1]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[AKAP13]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CCL20]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[ASAP1]] | +0.53 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ATP2B4]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[MAP2]] | +0.52 | +0.37 / +0.61 | both halves | 8e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA3]] | -0.58 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[GLE1]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[IKZF4]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[POLE3]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[ZNF213-AS1]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[EMC1-AS1]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[KLC4]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SUOX]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZBTB11]] | -0.48 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[GID8]] | -0.48 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[PRPSAP2]] | -0.48 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[C5orf15]] | -0.48 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UBE2E2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DIAPH2]] | B | DIAPH2 activity raises UBE2E2's level | lines that do not express DIAPH2 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without DIAPH2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000271204 |
| [[A4GALT]] | B | A4GALT activity raises UBE2E2's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 2.95× lower at baseline in the lines without A4GALT | 0.039 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[CCBE1]] | B | CCBE1 activity raises UBE2E2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.52× lower at baseline in the lines without CCBE1 | 0.078 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[ADRA1B]] | B | ADRA1B activity raises UBE2E2's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 2.49× lower at baseline in the lines without ADRA1B | 0.080 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[CCL20]] | B | CCL20 activity raises UBE2E2's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without CCL20 | 0.091 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBMS1]] | B | UBE2E2 activity raises RBMS1's level | lines that do not express UBE2E2 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without UBE2E2 | 0.082 | ⚠ within organs, on part of the lines; also absent: PRDM5, AMOTL1, RAB31 |
| [[DIAPH2]] | B | UBE2E2 activity raises DIAPH2's level | lines that do not express UBE2E2 (11) vs lines expressing it (39) | 1.15× lower at baseline in the lines without UBE2E2 | 0.094 | ⚠ within organs, on part of the lines; also absent: PRDM5, AMOTL1, RAB31 |
| [[ADRA1B]] | B | UBE2E2 activity raises ADRA1B's level | lines that do not express UBE2E2 (11) vs lines expressing it (39) | 2.45× lower at baseline in the lines without UBE2E2 | 0.099 | ⚠ within organs, on part of the lines; also absent: PRDM5, AMOTL1, RAB31 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, 10.8); signed map (14.4, 34.7). **Vector** length 129, 45.8% of its response variance represented; |z| ≥ 3 in 1,584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.9 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.8 | +10.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.6 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +12.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +8.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.7 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -35.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -14.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -13.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.0 | -15.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.1 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -9.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 E2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:23,203,020-23,591,794 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UbcH8, FLJ25157 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LR5](https://www.uniprot.org/uniprotkb/Q96LR5) (Ubiquitin-conjugating enzyme E2 E2):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-11'- and 'Lys-48'-, as well as 'Lys-63'-linked polyubiquitination. Catalyzes the ISGylation of influenza A virus NS1 protein.

**Summary**, from NCBI Gene [7325](https://www.ncbi.nlm.nih.gov/gene/7325):

> Enables ISG15 transferase activity and ubiquitin conjugating enzyme activity. Involved in protein modification by small protein conjugation. Acts upstream of or within DNA damage response and positive regulation of G1/S transition of mitotic cell cycle. Predicted to be active in nucleus. Implicated in type 2 diabetes mellitus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12478) · Entrez [7325](https://www.ncbi.nlm.nih.gov/gene/7325) · UniProt [Q96LR5](https://www.uniprot.org/uniprotkb/Q96LR5) · Ensembl [ENSG00000182247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182247)

## Data

Gene col 11264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11264); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11264]; `tensor/DDL_lfc|DDL_z.npy` [11264]; `embed/gene_vectors.npy` [11264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11264 or target_col == 11264). Every well: [[UBE2E2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2E2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
