---
symbol: "APTX"
type: "gene"
col: 5963
ensembl_id: "ENSG00000137074"
name: "aprataxin"
location: "9p21.1"
module: 89
arm: "+"
pooled_cpm: 91.52
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# APTX

*aprataxin* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +21.7, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.792× (z -6.5, q 6e-08, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.803× (z -4.1, q 0.003, down in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.107×, NCI-H23 0.355×, C-33 A 0.412×, A-427 0.450×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.273×, SW1417 0.369×, KATO III 0.426×, PANC-1 0.538×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CHP-212 0.0819×, HCT15 0.312×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.376×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCC1]] (+0.75, fdr 7e-06), [[XPNPEP3]] (+0.68, fdr 7e-06), [[TMEM11-DT]] (+0.66, fdr 1e-05); moves opposite to [[ISOC1]] (-0.58, fdr 1e-05), [[NAB1]] (-0.54, fdr 1e-05), [[AMOT]] (-0.54, fdr 7e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +21.7 | 0e+00 | 44/49 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +21.1 | 0e+00 | 45/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +16.7 | 0e+00 | 44/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +12.8 | 3e-35 | 36/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +10.4 | 3e-23 | 37/48 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +9.7 | 2e-20 | 33/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +9.4 | 3e-19 | 35/48 (KATO III, HOP62, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +8.6 | 7e-16 | 27/50 (A498, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +8.1 | 3e-14 | 32/48 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.32×** | +7.9 | 1e-13 | 28/48 (KATO III, NCI-H2347, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.24×** | +6.2 | 3e-08 | 28/48 (A549, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +5.8 | 3e-07 | 22/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.49×** | +5.3 | 5e-06 | 24/49 (A498, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.19× | +4.9 | 4e-05 | 19/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.45×** | +4.9 | 4e-05 | 20/48 (KATO III, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.8 | 5e-05 | 16/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +4.7 | 1e-04 | 14/49 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +4.3 | 5e-04 | 19/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.009 | 14/48 (KATO III, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.5 | 0.010 | 3/48 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.09× | +3.4 | 0.015 | 2/48 (H4, AN3 CA) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.09× | +3.4 | 0.017 | 3/48 (A549, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5963.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.107×, NCI-H23 0.355×, C-33 A 0.412×, A-427 0.450×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.273×, SW1417 0.369×, KATO III 0.426×, PANC-1 0.538×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CHP-212 0.0819×, HCT15 0.312×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.376×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.792×** | -6.5 | 6e-08 | 23/48 (PANC-1, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.818×** | -5.6 | 7e-06 | 22/44 (A-427, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.834× | -5.2 | 3e-05 | 23/49 (RKO, NCI-H23, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | 0.842× | -4.8 | 3e-04 | 20/47 (PANC-1, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.860× | -4.4 | 0.001 | 18/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | 0.860× | -4.3 | 0.001 | 19/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.803×** | -4.1 | 0.003 | 17/47 (LoVo, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.794× | -3.1 | 0.15 | 13/48 (HEC-1-A, HS-578T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 142 | 2 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +12.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.500× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[KATO III (line)]] | alt | 104 | 5 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.42× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -11.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 112 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +14.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.505× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[HCT15 (line)]] | alt | 135 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.376× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 53.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +15.7) | — |
| [[HOP62 (line)]] | alt | 79.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 3.95× (z +19.9) | — |
| [[SW480 (line)]] | alt | 111 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.29× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.578× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 73.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.75× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 74.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 83.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.8) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.172× (z -8.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 80.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.401× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 164 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 113 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.63× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -28.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 75.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -15.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 146 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.33× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.469× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0819× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 98.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +18.0) | — |
| [[LoVo (line)]] | wt | 107 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.04× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 90.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.36× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 122 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 56.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 83.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 67.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 86.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.71× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 70.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.87× (z +11.1) | — |
| [[SW48 (line)]] | wt | 95.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.69× (z +11.2) | — |
| [[A549 (line)]] | wt | 93.0 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C-33 A (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 46.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.16× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 149 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +20.6) | — |
| [[HepG2_C3A (line)]] | wt | 78.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 72.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 83.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 88.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 72.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 43.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 66.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.12× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCC1]] | +0.75 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[XPNPEP3]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[TMEM11-DT]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ELMOD3]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PLD5P1]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MAFIP]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZNF586]] | +0.64 | +0.57 / +0.60 | both halves | 9e-06 | same gene group |
| [[GARS1-DT]] | +0.64 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[SLC25A17]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | +0.63 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[LRRC41]] | +0.62 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[AGAP5]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISOC1]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[NAB1]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[AMOT]] | -0.54 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[PTGER4]] | -0.53 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[PNPLA2]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[HMSD]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZMIZ2]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[KLF12]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 | same gene group |
| [[PTBP3]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.6, 20.5); signed map (0.6, -3.2). **Vector** length 103, 27.4% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.1 | +21.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.6 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.7 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~77% of this change | +4.0 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -9.2 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.9 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | -4.8 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +2.6 |
|  | [[OTS514 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | aprataxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:32,886,601-33,025,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20157, AOA, AOA1, EAOH, EOAHA; previously AXA1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Histidine triad superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2E3](https://www.uniprot.org/uniprotkb/Q7Z2E3) (Aprataxin):

> DNA-binding protein involved in single-strand DNA break repair, double-strand DNA break repair and base excision repair. Resolves abortive DNA ligation intermediates formed either at base excision sites, or when DNA ligases attempt to repair non-ligatable breaks induced by reactive oxygen species. Catalyzes the release of adenylate groups covalently linked to 5'-phosphate termini, resulting in the production of 5'-phosphate termini that can be efficiently rejoined. Also able to hydrolyze …

**Summary**, from NCBI Gene [54840](https://www.ncbi.nlm.nih.gov/gene/54840):

> This gene encodes a member of the histidine triad (HIT) superfamily. The encoded protein may play a role in single-stranded DNA repair through its nucleotide-binding activity and its diadenosine polyphosphate hydrolase activity. Mutations in this gene have been associated with ataxia-ocular apraxia. Alternatively spliced transcript variants have been identified for this gene.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:15984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15984) · Entrez [54840](https://www.ncbi.nlm.nih.gov/gene/54840) · UniProt [Q7Z2E3](https://www.uniprot.org/uniprotkb/Q7Z2E3) · Ensembl [ENSG00000137074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137074)

## Data

Gene col 5963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5963); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5963]; `tensor/DDL_lfc|DDL_z.npy` [5963]; `embed/gene_vectors.npy` [5963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5963 or target_col == 5963). Every well: [[APTX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APTX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
