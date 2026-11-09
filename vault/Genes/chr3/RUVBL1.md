---
symbol: "RUVBL1"
type: "gene"
col: 10650
ensembl_id: "ENSG00000175792"
name: "RuvB like AAA ATPase 1"
location: "3q21.3"
module: 4
arm: "+"
pooled_cpm: 33.33
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RUVBL1

*RuvB like AAA ATPase 1* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.76× (z +22.0, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.37× (z +12.2, q 4e-32, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.187×, SW48 0.185×; ⚠ cell-cycle shift, would explain all of this change); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0785×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.411×; ⚠ cell-cycle shift, explains ~0% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0964×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FARSB]] (+0.84, fdr 7e-06), [[ATIC]] (+0.82, fdr 7e-06), [[PPIL1]] (+0.77, fdr 7e-06); moves opposite to [[RSRP1]] (-0.71, fdr 8e-06), [[SIRT2]] (-0.70, fdr 7e-06), [[AAMDC]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.76×** | +22.0 | 0e+00 | 43/43 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.50×** | +20.4 | 0e+00 | 39/39 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.03×** | +14.5 | 3e-45 | 39/42 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.37×** | +12.2 | 4e-32 | 45/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.18×** | +11.0 | 5e-26 | 39/48 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.96×** | +9.5 | 2e-19 | 39/48 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.94×** | +9.0 | 2e-17 | 41/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.83×** | +8.5 | 1e-15 | 36/47 (HOP62, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.72×** | +7.4 | 9e-12 | 29/47 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.74×** | +7.2 | 3e-11 | 35/47 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +7.0 | 2e-10 | 34/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +6.3 | 2e-08 | 35/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 2e-05 | 25/47 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.44×** | +4.9 | 5e-05 | 28/46 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.8 | 7e-05 | 21/48 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +4.7 | 9e-05 | 23/47 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.71×** | +4.0 | 0.002 | 17/47 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.007 | 13/47 (NCI-H2347, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.009 | 16/47 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.18× | +3.3 | 0.021 | 14/48 (NCI-H2030, A498, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.025 | 19/47 (NCI-H1573, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.026 | 10/45 (A-172, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.038 | 10/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.040 | 18/47 (SNU-423, HS-578T, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.086 | 6/48 (NCI-H1573, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10650.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.187×, SW48 0.185×; ⚠ cell-cycle shift, would explain all of this change); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0785×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.411×; ⚠ cell-cycle shift, explains ~0% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0964×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.789× | -3.4 | 0.23 | 20/48 (NCI-H460, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.794× | -3.3 | 0.23 | 16/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.851× | -3.2 | 0.23 | 14/48 (LS 180, KATO III, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.856× | -3.1 | 0.26 | 10/48 (A498, HEC-1-A, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 19.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.53× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.85× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 21.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.35× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.62× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.86× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.86× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 38.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.14× (z +11.1) | — |
| [[A-172 (line)]] | wt | 23.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.60× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 26.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.20× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.71× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 27.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 21.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.22× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 131 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 18.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.04× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 46.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 56.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 13.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.12× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 18.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 30.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 21.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 66.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 31.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.19× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 67.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.216× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.21× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0964× (z -9.0) |
| [[H4 (line)]] | wt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.37× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0785× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.31× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[ATIC]] | +0.82 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.77 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.77 | +0.76 / +0.76 | both halves | 7e-06 | STRING 902 |
| [[NAA15]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[EBNA1BP2]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 | STRING 417 |
| [[DDX10]] | +0.73 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[WDR77]] | +0.73 | +0.75 / +0.72 | both halves | 7e-06 | pathway: Chromatin modifying enzymes; STRING 427 |
| [[MYBBP1A]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CCT5]] | +0.72 | +0.78 / +0.69 | both halves | 7e-06 | STRING 864 |
| [[C1QBP]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | STRING 486 |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.71 | -0.57 / -0.70 | both halves | 8e-06 |  |
| [[SIRT2]] | -0.70 | -0.75 / -0.70 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.70 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.69 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[TRNAU1AP]] | -0.66 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ZNF821]] | -0.65 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[KLC4]] | -0.65 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.64 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[TMEM106A]] | -0.64 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[SERF2]] | -0.64 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[RABAC1]] | -0.64 | -0.64 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.803). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.2, -34.7); signed map (-6.9, -45.8). **Vector** length 99.3, 27.2% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.55 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.51 to 7); *Folding of actin by CCT/TriC* (reactome, mean cos +0.62 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.7 | +22.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.5 | +20.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -0.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RuvB like AAA ATPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:128,064,778-128,153,914 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIP49, NMP238, RVB1, TIP49a, Pontin52, ECP54, TIH1, Rvb1 |
| Gene groups (HGNC) | AAA ATPases; INO80 complex subunits; Helicases; SRCAP complex subunits; R2TP complex; Tip60/Nua4 histone acetyltransferase complex subunits |
| Reactome | 20 pathways, smallest: Telomere Extension By Telomerase; DNA Damage Recognition in GG-NER; Deposition of new CENPA-containing nucleosomes at the centromere |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y265](https://www.uniprot.org/uniprotkb/Q9Y265) (RuvB-like 1):

> Possesses single-stranded DNA-stimulated ATPase and ATP-dependent DNA helicase (3' to 5') activity; hexamerization is thought to be critical for ATP hydrolysis and adjacent subunits in the ring-like structure contribute to the ATPase activity. Component of the NuA4 histone acetyltransferase complex which is involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. This modification may both alter nucleosome-DNA interactions and promote …

**Summary**, from NCBI Gene [8607](https://www.ncbi.nlm.nih.gov/gene/8607):

> This gene encodes a protein that has both DNA-dependent ATPase and DNA helicase activities and belongs to the ATPases associated with diverse cellular activities (AAA+) protein family. The encoded protein associates with several multisubunit transcriptional complexes and with protein complexes involved in both ATP-dependent remodeling and histone modification. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:10474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10474) · Entrez [8607](https://www.ncbi.nlm.nih.gov/gene/8607) · UniProt [Q9Y265](https://www.uniprot.org/uniprotkb/Q9Y265) · Ensembl [ENSG00000175792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175792)

## Data

Gene col 10650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10650); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10650]; `tensor/DDL_lfc|DDL_z.npy` [10650]; `embed/gene_vectors.npy` [10650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10650 or target_col == 10650). Every well: [[RUVBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUVBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
