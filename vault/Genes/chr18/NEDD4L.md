---
symbol: "NEDD4L"
type: "gene"
col: 555
ensembl_id: "ENSG00000049759"
name: "NEDD4 like E3 ubiquitin protein ligase"
location: "18q21.31"
module: 120
arm: "+"
pooled_cpm: 328.69
n_lines_expressing: 48
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# NEDD4L

*NEDD4 like E3 ubiquitin protein ligase* — 18q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.15× (z +32.6, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.470× (z -14.6, q 1e-45, down in 33 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.625× (z -4.9, q 7e-05, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXP1]] (+0.60, fdr 2e-05), [[HIVEP2]] (+0.56, fdr 7e-06), [[CRIM1]] (+0.54, fdr 1e-05); moves opposite to [[ATPAF1]] (-0.55, fdr 2e-05), [[TXNDC15]] (-0.54, fdr 2e-05), [[RINT1]] (-0.53, fdr 1e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RUNX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.15×** | +32.6 | 0e+00 | 43/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.53×** | +19.7 | 0e+00 | 47/47 (PANC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.59×** | +18.4 | 0e+00 | 43/46 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +16.3 | 0e+00 | 41/46 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +12.9 | 5e-36 | 37/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.88×** | +12.7 | 4e-35 | 40/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.88×** | +12.7 | 5e-35 | 38/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +10.6 | 2e-24 | 39/45 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +10.1 | 4e-22 | 38/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +9.8 | 6e-21 | 41/46 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +8.3 | 4e-15 | 32/46 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +7.6 | 2e-12 | 31/46 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +7.0 | 1e-10 | 30/46 (PANC-1, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.5 | 3e-09 | 32/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 4e-08 | 28/46 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +5.5 | 1e-06 | 30/46 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 4e-06 | 27/46 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -14.6 | 1e-45 | 33/42 (C-33 A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.556×** | -11.8 | 8e-30 | 39/47 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -10.7 | 1e-24 | 40/45 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.576×** | -10.3 | 1e-22 | 35/43 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.725×** | -6.5 | 1e-08 | 29/46 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.625×** | -4.9 | 7e-05 | 31/46 (SHP-77, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.728×** | -4.6 | 4e-04 | 32/46 (NCI-H2030, SHP-77, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.806×** | -4.3 | 1e-03 | 23/46 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.671×** | -4.2 | 0.002 | 26/46 (NCI-H2347, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.813×** | -4.2 | 0.002 | 22/46 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.682×** | -4.0 | 0.003 | 22/46 (SW1417, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.682×** | -4.0 | 0.003 | 28/46 (SHP-77, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.838× | -3.6 | 0.016 | 22/46 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -3.5 | 0.022 | 2/48 (NCI-H23, NCI-H2122) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.890× | -3.3 | 0.033 | 20/47 (LOX-IMVI, A549, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.734×** | -3.3 | 0.040 | 19/46 (SHP-77, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.858× | -3.1 | 0.069 | 15/47 (NCI-H1573, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 145 | 16 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +35.7) | — |
| [[NCI-H460 (line)]] | wt | 297 | 10 (3 ⚠) | 5 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.82× (z +17.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.44× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -13.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 302 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +31.2) | — |
| [[AsPC-1 (line)]] | alt | 133 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +32.2) | — |
| [[hTERT-HPNE (line)]] | wt | 285 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +24.3) | — |
| [[J82 (line)]] | alt | 480 | 7 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +25.1) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 288 | 10 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 432 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +24.6) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 644 | 8 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.89× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -13.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 423 | 5 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -12.4) ⚠ cell-cycle shift, explains ~3% of this change |
| [[A549 (line)]] | wt | 290 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +25.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -12.5) ⚠ cell-cycle shift, explains ~3% of this change |
| [[C32 (line)]] | wt | 997 | 3 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 8.64× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.452× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 378 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +25.8) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -11.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 144 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +27.7) | — |
| [[Hs 766T (line)]] | wt | 201 | 9 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 18.5× (z +17.6) | — |
| [[NCI-H1573 (line)]] | alt | 351 | 8 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.8× (z +17.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.485× (z -8.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 154 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +21.3) | — |
| [[SK-MEL-2 (line)]] | alt | 686 | 7 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 457 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +23.5) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 264 | 5 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.85× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -11.1) ⚠ cell-cycle shift, explains ~3% of this change |
| [[NCI-H2030 (line)]] | alt | 570 | 5 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.282× (z -13.8) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 373 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.558× (z -10.6) |
| [[SW 900 (line)]] | alt | 165 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +19.2) | — |
| [[H4 (line)]] | wt | 323 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +23.8) | — |
| [[KATO III (line)]] | alt | 481 | 4 | 3 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.45× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.7) ⚠ cell-cycle shift, explains ~3% of this change |
| [[NCI-H2347 (line)]] | alt | 360 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +23.7) | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 420 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 85.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +31.6) | — |
| [[HCT15 (line)]] | alt | 261 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.1) | — |
| [[HepG2_C3A (line)]] | wt | 689 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.256× (z -15.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 329 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 209 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +32.3) | — |
| [[A-172 (line)]] | wt | 145 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +24.6) | — |
| [[COLO 205 (line)]] | alt | 195 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.66× (z +16.1) | — |
| [[A-427 (line)]] | wt | 117 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 787 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.4) ⚠ cell-cycle shift, explains ~3% of this change |
| [[HT-29 (line)]] | alt | 385 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.6) ⚠ cell-cycle shift, explains ~3% of this change |
| [[LOX-IMVI (line)]] | wt | 727 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.4) ⚠ cell-cycle shift, explains ~3% of this change |
| [[AN3 CA (line)]] | alt | 252 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.2) | — |
| [[C-33 A (line)]] | alt | 304 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -18.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 157 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.55× (z +11.5) | — |
| [[RKO (line)]] | wt | 145 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -23.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.2) | — |
| [[SW 1088 (line)]] | alt | 360 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +11.6) | — |
| [[SW 1271 (line)]] | alt | 369 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 376 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 67.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXP1]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[HIVEP2]] | +0.56 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CRIM1]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[WWC1]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TRIO]] | +0.53 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[SRGAP1]] | +0.52 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[MAGI1]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CLDN1]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NCAM1]] | +0.52 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[C11orf96]] | +0.51 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[SGK1]] | +0.51 | +0.38 / +0.47 | both halves | 7e-05 | pathway: Ion channel transport; STRING 999 |
| [[SASH1]] | +0.51 | +0.39 / +0.52 | both halves | 6e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATPAF1]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TXNDC15]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RINT1]] | -0.53 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[MTO1]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[RNF139-DT]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CWF19L1]] | -0.51 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[GLE1]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[SLC30A6]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[METTL21EP-1]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[NUP133]] | -0.48 | -0.45 / -0.49 | both halves | 3e-05 | pathway: HIV Infection |
| [[SLC30A5]] | -0.48 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CHFR]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNX1]] | B | RUNX1 activity raises NEDD4L's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without RUNX1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[DOCK4]] | B | DOCK4 activity raises NEDD4L's level | lines that do not express DOCK4 (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without DOCK4 | 0.063 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[CLDN1]] | B | CLDN1 activity raises NEDD4L's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 1.27× lower at baseline in the lines without CLDN1 | 0.064 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[PTGER4]] | B | PTGER4 activity raises NEDD4L's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without PTGER4 | 0.081 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 10.0); signed map (19.7, 24.7). **Vector** length 112, 37.8% of its response variance represented; |z| ≥ 3 in 1,840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +7.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +19.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.2 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.5 | +1.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.5 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.7 | -10.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.0 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -4.4 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.2 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.1 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | NEDD4 like E3 ubiquitin protein ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.31 — chr18:58,044,226-58,401,540 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0439, RSP5, NEDD4-2 |
| Gene groups (HGNC) | C2 domain containing; Nedd4 family E3 ubiquitin protein ligases |
| Hallmark sets | HYPOXIA |
| Reactome | 17 pathways, smallest: Downregulation of TGF-beta receptor signaling; Budding and maturation of HIV virion; Downregulation of SMAD2/3:SMAD4 transcriptional activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PU5](https://www.uniprot.org/uniprotkb/Q96PU5) (E3 ubiquitin-protein ligase NEDD4-like):

> E3 ubiquitin-protein ligase that mediates the polyubiquitination of lysine and cysteine residues on target proteins and is thereby implicated in the regulation of various signaling pathways including autophagy, innate immunity or DNA repair. Inhibits TGF-beta signaling by triggering SMAD2 and TGFBR1 ubiquitination and proteasome-dependent degradation. Down-regulates autophagy and cell growth by ubiquitinating and reducing cellular ULK1 or ASCT2 levels. Promotes ubiquitination and …

**Summary**, from NCBI Gene [23327](https://www.ncbi.nlm.nih.gov/gene/23327):

> This gene encodes a member of the Nedd4 family of HECT domain E3 ubiquitin ligases. HECT domain E3 ubiquitin ligases transfer ubiquitin from E2 ubiquitin-conjugating enzymes to protein substrates, thus targeting specific proteins for lysosomal degradation. The encoded protein mediates the ubiquitination of multiple target substrates and plays a critical role in epithelial sodium transport by regulating the cell surface expression of the epithelial sodium channel, ENaC. Single nucleotide …

**Accessions** — [HGNC:7728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7728) · Entrez [23327](https://www.ncbi.nlm.nih.gov/gene/23327) · UniProt [Q96PU5](https://www.uniprot.org/uniprotkb/Q96PU5) · Ensembl [ENSG00000049759](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049759)

## Data

Gene col 555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 555); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 555]; `tensor/DDL_lfc|DDL_z.npy` [555]; `embed/gene_vectors.npy` [555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 555 or target_col == 555). Every well: [[NEDD4L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEDD4L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
