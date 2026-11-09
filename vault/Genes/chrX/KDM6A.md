---
symbol: "KDM6A"
type: "gene"
col: 7143
ensembl_id: "ENSG00000147050"
name: "lysine demethylase 6A"
location: "Xp11.3"
module: 69
arm: "+"
pooled_cpm: 250.58
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# KDM6A

*lysine demethylase 6A* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +12.9, q 3e-35, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.269× (z -16.3, q 0e+00, down in 43 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.444× (z -5.1, q 4e-05, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HBP1]] (+0.71, fdr 7e-06), [[NEK7]] (+0.70, fdr 8e-06), [[CHASERR]] (+0.66, fdr 7e-06); moves opposite to [[RRP1B]] (-0.67, fdr 7e-06), [[ANKS6]] (-0.60, fdr 8e-05), [[POLR3A]] (-0.60, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +12.9 | 3e-35 | 45/47 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.67×** | +12.7 | 3e-34 | 47/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +9.1 | 3e-17 | 41/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.97×** | +8.7 | 7e-16 | 46/48 (COLO 205, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.81×** | +8.4 | 5e-15 | 45/47 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +8.3 | 1e-14 | 43/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +7.5 | 6e-12 | 42/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +6.5 | 7e-09 | 38/47 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.8 | 5e-07 | 38/46 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.6 | 2e-06 | 35/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 36/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 0.001 | 29/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.026 | 24/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.042 | 27/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +3.0 | 0.093 | 23/47 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.093 | 24/47 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.269×** | -16.3 | 0e+00 | 43/43 (C-33 A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.314×** | -14.9 | 0e+00 | 48/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.496×** | -9.0 | 3e-17 | 46/47 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -7.8 | 8e-13 | 46/46 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.444×** | -5.1 | 4e-05 | 42/47 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.688×** | -4.8 | 1e-04 | 38/47 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.473×** | -4.7 | 2e-04 | 44/47 (NCI-H2347, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.480×** | -4.6 | 3e-04 | 41/47 (NCI-H2347, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.682×** | -4.6 | 3e-04 | 29/44 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.504×** | -4.3 | 1e-03 | 40/47 (LoVo, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.006 | 35/47 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.751×** | -3.7 | 0.011 | 31/47 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.819×** | -3.6 | 0.013 | 30/47 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.786×** | -3.1 | 0.078 | 25/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 352 | 14 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.30× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -14.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 292 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -15.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 290 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -16.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 176 | 5 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 201 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.04× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 222 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 223 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -10.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 241 | 6 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -13.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 141 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.454× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 295 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.64× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 150 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 184 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 205 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 399 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -20.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 206 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 307 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -13.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 395 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.19× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.102× (z -15.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 199 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 414 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -16.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 245 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 326 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -20.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 370 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -16.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 271 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 147 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 297 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 302 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -14.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 154 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 199 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -15.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 261 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -16.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 299 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0966× (z -20.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 358 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -15.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 235 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 380 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -17.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 308 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -18.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 220 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.38× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 430 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -15.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 175 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.04× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 245 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -20.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 218 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -12.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 213 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.254× (z -8.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 147 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 270 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -15.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HBP1]] | +0.71 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[NEK7]] | +0.70 | +0.58 / +0.79 | both halves | 8e-06 |  |
| [[CHASERR]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.66 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[ELF2]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.65 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[PCMTD1]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CYLD]] | +0.63 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[TMEM59]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[WAC]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TLK2]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ARID4B]] | +0.62 | +0.59 / +0.50 | both halves | 1e-05 | pathway: Chromatin modifying enzymes; STRING 436 |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.67 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[ANKS6]] | -0.60 | -0.37 / -0.62 | both halves | 8e-05 |  |
| [[POLR3A]] | -0.60 | -0.49 / -0.65 | both halves | 1e-05 | STRING 511 |
| [[NCBP2]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ZNF473]] | -0.57 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[GNPNAT1]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[EIF2B3]] | -0.56 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[EEFSEC]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PDCD11]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 | STRING 532 |
| [[NLE1]] | -0.56 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[MPHOSPH6]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 | pathway: Affinity selection of immunoglobulins |
| [[RMND1]] | -0.55 | -0.33 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.0, -42.0); signed map (-13.9, 11.4). **Vector** length 87.2, 39.5% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | -14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +5.2 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.4 | -9.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.0 | -4.7 |
|  | [[EX229 (drug)]] 5 µM |  | -6.9 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.8 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.7 | -5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:44,873,188-45,112,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously UTX |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Lysine demethylase 6 family |
| Reactome | 17 pathways, smallest: Chromatin modifications during the maternal to zygotic transition (MZT); HDMs demethylate histones; Formation of WDR5-containing histone-modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15550](https://www.uniprot.org/uniprotkb/O15550) (Lysine-specific demethylase 6A):

> Histone demethylase that specifically demethylates 'Lys-27' of histone H3, thereby playing a central role in histone code. Demethylates trimethylated and dimethylated but not monomethylated H3 'Lys-27'. Plays a central role in regulation of posterior development, by regulating HOX gene expression. Demethylation of 'Lys-27' of histone H3 is concomitant with methylation of 'Lys-4' of histone H3, and regulates the recruitment of the PRC1 complex and monoubiquitination of histone H2A. Plays a …

**Summary**, from NCBI Gene [7403](https://www.ncbi.nlm.nih.gov/gene/7403):

> This gene is located on the X chromosome and is the corresponding locus to a Y-linked gene which encodes a tetratricopeptide repeat (TPR) protein. The encoded protein of this gene contains a JmjC-domain and catalyzes the demethylation of tri/dimethylated histone H3. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:12637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12637) · Entrez [7403](https://www.ncbi.nlm.nih.gov/gene/7403) · UniProt [O15550](https://www.uniprot.org/uniprotkb/O15550) · Ensembl [ENSG00000147050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147050)

## Data

Gene col 7143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7143); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7143]; `tensor/DDL_lfc|DDL_z.npy` [7143]; `embed/gene_vectors.npy` [7143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7143 or target_col == 7143). Every well: [[KDM6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
