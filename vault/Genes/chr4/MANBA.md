---
symbol: "MANBA"
type: "gene"
col: 3044
ensembl_id: "ENSG00000109323"
name: "mannosidase beta"
location: "4q24"
module: 169
arm: "+"
pooled_cpm: 83.99
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 16
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# MANBA

*mannosidase beta* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.44× (z +18.9, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.466× (z -14.3, q 2e-43, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.682× (z -7.4, q 2e-11, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNASET2]] (+0.68, fdr 1e-05), [[HELZ]] (+0.65, fdr 7e-06), [[MINDY3]] (+0.64, fdr 7e-06); moves opposite to [[PIGL]] (-0.60, fdr 1e-05), [[ANAPC7]] (-0.57, fdr 2e-05), [[TNFRSF12A]] (-0.54, fdr 1e-05).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.44×** | +18.9 | 0e+00 | 49/49 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.36×** | +12.3 | 2e-32 | 45/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +9.8 | 2e-20 | 35/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.5 | 2e-15 | 29/49 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +8.4 | 4e-15 | 30/48 (HT-29, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.6 | 3e-09 | 32/48 (HS-578T, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +6.5 | 6e-09 | 31/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +6.4 | 1e-08 | 32/48 (RKO, KATO III, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.2 | 5e-08 | 26/50 (LS 180, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.23×** | +5.7 | 5e-07 | 27/48 (J82, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.4 | 4e-06 | 25/48 (RKO, LoVo, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +5.2 | 1e-05 | 24/48 (RKO, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.8 | 8e-05 | 28/48 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.4 | 4e-04 | 27/49 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.4 | 4e-04 | 27/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 8e-04 | 23/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.007 | 21/48 (KATO III, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -14.3 | 2e-43 | 39/44 (C32, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.525×** | -12.5 | 1e-33 | 42/49 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.682×** | -7.4 | 2e-11 | 36/48 (HCT15, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.696×** | -7.0 | 3e-10 | 36/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.692×** | -6.9 | 6e-10 | 30/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.736×** | -6.0 | 2e-07 | 29/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.748×** | -5.6 | 1e-06 | 30/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.771×** | -4.7 | 2e-04 | 27/45 (Panc 03.27, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.788×** | -4.6 | 2e-04 | 27/48 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.864× | -4.0 | 0.003 | 12/48 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **0.793×** | -4.0 | 0.004 | 25/48 (HCT15, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.8 | 0.006 | 0/50 | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.873× | -3.7 | 0.008 | 10/48 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.825×** | -3.6 | 0.013 | 21/47 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.838× | -3.4 | 0.022 | 18/47 (NCI-H23, C32, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.820×** | -3.4 | 0.023 | 16/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.825×** | -3.3 | 0.030 | 18/48 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.750×** | -3.2 | 0.036 | 14/48 (HOP62, C32, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.736×** | -3.1 | 0.052 | 17/46 (RPMI-7951, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.900× | -2.9 | 0.095 | 5/49 (A-427, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 235 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.391× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 57.3 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +17.2) | [[Digitoxin (drug)]] 5 µM 0.320× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 112 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 139 | 2 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.41× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 77.0 | 2 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 17.0× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -12.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 97.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -8.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 36.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 16.0× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.49× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 86.3 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.0× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -12.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 49.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.8× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -14.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 68.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 76.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.2× (z +17.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.44× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 104 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.7× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 56.4 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.2× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 83.2 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.40× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.364× (z -9.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 97.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 118 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.09× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -11.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 67.7 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 8.33× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 100 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[RKO (line)]] | wt | 79.7 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.80× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -19.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 99.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.2× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -15.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 76.2 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +11.7) | — |
| [[SW48 (line)]] | wt | 150 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -12.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 115 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.32× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -10.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 86.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 73.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.46× (z +10.2) | [[Digitoxin (drug)]] 0.05 µM 0.415× (z -9.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H23 (line)]] | alt | 75.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.5× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 70.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -14.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 54.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.42× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 89.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[AN3 CA (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -9.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 63.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 77.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 93.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 50.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.00× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 71.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.19× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 50.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 69.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.84× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0617× (z -10.8) |
| [[SW 1271 (line)]] | alt | 64.3 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0816× (z -9.5) |
| [[BT-474 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASET2]] | +0.68 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[HELZ]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[POLR1D]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[HERC3]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[PCOLCE]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ORC4]] | +0.59 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[DCAF5]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[BMT2]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[GGA2]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[MXI1]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RELCH]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGL]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TNFRSF12A]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[AKIRIN1]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[WDR82]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ZSCAN5A]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[RBM12]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[EIF3J]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CUEDC1]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[PROSER3]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[IPO9]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ATXN10]] | -0.50 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.7, -22.3); signed map (-37.9, 22.2). **Vector** length 126, 41.0% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.6 | +18.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.8 | +12.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.3 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | +6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.4 | +2.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.7 | -7.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -7.4 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -7.1 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -6.8 | -6.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -6.1 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:102,630,770-102,760,994 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mannosidases type beta |
| Reactome | 4 pathways, smallest: Lysosomal oligosaccharide catabolism; Metabolism of carbohydrates and carbohydrate derivatives; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O00462](https://www.uniprot.org/uniprotkb/O00462) (Beta-mannosidase):

> Exoglycosidase that cleaves the single beta-linked mannose residue from the non-reducing end of all N-linked glycoprotein oligosaccharides.

**Summary**, from NCBI Gene [4126](https://www.ncbi.nlm.nih.gov/gene/4126):

> This gene encodes a member of the glycosyl hydrolase 2 family. The encoded protein localizes to the lysosome where it is the final exoglycosidase in the pathway for N-linked glycoprotein oligosaccharide catabolism. Mutations in this gene are associated with beta-mannosidosis, a lysosomal storage disease that has a wide spectrum of neurological involvement. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6831) · Entrez [4126](https://www.ncbi.nlm.nih.gov/gene/4126) · UniProt [O00462](https://www.uniprot.org/uniprotkb/O00462) · Ensembl [ENSG00000109323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109323)

## Data

Gene col 3044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3044); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3044]; `tensor/DDL_lfc|DDL_z.npy` [3044]; `embed/gene_vectors.npy` [3044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3044 or target_col == 3044). Every well: [[MANBA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MANBA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
