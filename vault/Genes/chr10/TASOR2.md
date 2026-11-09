---
symbol: "TASOR2"
type: "gene"
col: 2911
ensembl_id: "ENSG00000108021"
name: "transcription activation suppressor family member 2"
location: "10p15.1"
module: 5
arm: "+"
pooled_cpm: 180.56
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 5
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TASOR2

*transcription activation suppressor family member 2* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.03× (z +20.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.566× (z -16.8, q 0e+00, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (COLO 205 0.0486×, NCI-H460 0.436×, RKO 0.385×, NCI-H1573 0.382×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.218×, A-427 0.301×, SK-MEL-2 0.339×, C-33 A 0.267×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.247×, C-33 A 0.342×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (RKO 0.426×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.695×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPRC1]] (+0.71, fdr 7e-06), [[ATR]] (+0.69, fdr 7e-06), [[PINX1]] (+0.68, fdr 7e-06); moves opposite to [[LINC00674]] (-0.59, fdr 9e-06), [[MAPK3]] (-0.59, fdr 1e-05), [[VAMP7]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2911.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +20.1 | 0e+00 | 43/48 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +17.9 | 0e+00 | 37/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +17.4 | 0e+00 | 45/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +17.1 | 0e+00 | 42/48 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +16.4 | 0e+00 | 42/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +14.0 | 2e-42 | 43/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +13.3 | 1e-38 | 42/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.50×** | +11.9 | 8e-31 | 36/48 (BT-474, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.49×** | +11.9 | 1e-30 | 36/48 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +10.5 | 4e-24 | 33/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +10.3 | 2e-23 | 39/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +10.2 | 7e-23 | 41/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.41×** | +10.2 | 7e-23 | 35/48 (SNU-423, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +9.8 | 6e-21 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.26×** | +9.7 | 7e-21 | 27/49 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +8.2 | 8e-15 | 30/48 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +8.1 | 2e-14 | 43/48 (KATO III, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +7.0 | 7e-11 | 33/49 (COLO 205, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +6.6 | 1e-09 | 27/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +6.5 | 2e-09 | 27/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +6.3 | 9e-09 | 24/48 (SW480, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2911.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (COLO 205 0.0486×, NCI-H460 0.436×, RKO 0.385×, NCI-H1573 0.382×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.218×, A-427 0.301×, SK-MEL-2 0.339×, C-33 A 0.267×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.247×, C-33 A 0.342×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (RKO 0.426×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.695×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.566×** | -16.8 | 0e+00 | 42/49 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -13.0 | 5e-36 | 34/44 (SHP-77, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.690×** | -9.6 | 1e-19 | 34/45 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.828×** | -7.9 | 3e-13 | 27/48 (AsPC-1, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.825×** | -5.5 | 5e-06 | 24/47 (HS-578T, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.838× | -5.2 | 2e-05 | 21/49 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.843× | -5.1 | 3e-05 | 19/48 (SNU-423, A498, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.862× | -4.4 | 7e-04 | 18/47 (LS 180, H4, …) | rises with dose | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.874× | -4.0 | 0.004 | 14/48 (J82, A498, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.879× | -3.8 | 0.007 | 18/48 (J82, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.881× | -3.6 | 0.015 | 13/48 (A498, CHP-212, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.836× | -3.5 | 0.018 | 11/47 (SK-MEL-2, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.965× | -3.3 | 0.044 | 3/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.891× | -3.2 | 0.051 | 12/48 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.902× | -3.1 | 0.078 | 12/48 (SNU-423, KATO III, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.857× | -3.1 | 0.078 | 6/48 (J82, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 173 | 10 (5 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.07× (z +12.5) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.06× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 120 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +17.3) | — |
| [[NCI-H1792 (line)]] | alt | 216 | 12 (4 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.54× (z +17.4) | — |
| [[PANC-1 (line)]] | alt | 193 | 10 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -11.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 229 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +19.0) | — |
| [[AsPC-1 (line)]] | alt | 131 | 8 (4 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.66× (z +12.4) | [[Selinexor (drug)]] 5 µM 0.594× (z -9.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[CFPAC-1 (line)]] | alt | 148 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +22.6) | — |
| [[J82 (line)]] | alt | 241 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -13.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 155 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.3) | — |
| [[SW480 (line)]] | alt | 146 | 8 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.22× (z +13.8) | — |
| [[A-172 (line)]] | wt | 190 | 5 (3 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.99× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -13.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 216 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -11.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 174 | 4 | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.04× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 213 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.88× (z +17.5) | — |
| [[SW 900 (line)]] | alt | 102 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.5) | — |
| [[A498 (line)]] | wt | 207 | 4 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.09× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.519× (z -10.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 160 | 5 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.31× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0486× (z -28.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 108 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 126 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 125 | 6 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.26× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 216 | 5 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.13× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 114 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 290 | 3 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.15× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.519× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 308 | 2 | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.37× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -16.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 225 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 153 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 244 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.414× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 139 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +19.6) | — |
| [[A-427 (line)]] | wt | 260 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -18.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 143 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.10× (z +11.3) | — |
| [[LoVo (line)]] | wt | 195 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 304 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -17.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 152 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 155 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.27× (z +9.0) | [[Docetaxel (drug)]] 0.05 µM 0.475× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.8) | — |
| [[RKO (line)]] | wt | 329 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -12.3) |
| [[CHP-212 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 189 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.34× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 159 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.8) | — |
| [[KATO III (line)]] | alt | 115 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -22.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 232 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 1.85× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 215 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 98.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 203 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPRC1]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[ATR]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[PINX1]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[SDAD1]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[LTV1]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[NIP7]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PNO1]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PUS1]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[WDR4]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[MRTO4]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[GTPBP4]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[DDX31]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00674]] | -0.59 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[MAPK3]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[VAMP7]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ATP6V1B2]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[CCNG2]] | -0.54 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[VAMP1]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ABI1]] | -0.53 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[MXD1]] | -0.53 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CALCOCO1]] | -0.52 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[FKBP8]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[RAB11A]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[NPTN]] | -0.51 | -0.56 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.2, -36.8); signed map (-0.1, -49.6). **Vector** length 105, 35.2% of its response variance represented; |z| ≥ 3 in 1,593 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.54 to 13); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 11); *ribosome biogenesis* (control, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +17.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.7 | +9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +5.2 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -9.1 | -7.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -5.0 | -3.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.5 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | +17.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | transcription activation suppressor family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:5,684,731-5,763,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20360, bA318E3.2, KIAA2006; previously C10orf18, FAM208B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VWN6](https://www.uniprot.org/uniprotkb/Q5VWN6) (Protein TASOR 2):

> Core component of the HUSH2 complex, a multiprotein complex that mediates epigenetic repression of interferon-stimulated genes. TASOR2 is recruited to interferon-stimulated genes by IRF2, leading to transcriptional silencing by the HUSH2 complex via a H3K9me3-independent mechanism. Within the HUSH2 complex, TASOR2 acts as the central scaffold, which recruits MPHOSPH8 and PPHLN1.

**Summary**, from NCBI Gene [54906](https://www.ncbi.nlm.nih.gov/gene/54906):

> Enables protein-macromolecule adaptor activity. Involved in negative regulation of gene expression, epigenetic and negative regulation of type I interferon production. Located in cytosol and nucleoplasm. Part of HUSH2 complex. Is active in chromatin and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23484) · Entrez [54906](https://www.ncbi.nlm.nih.gov/gene/54906) · UniProt [Q5VWN6](https://www.uniprot.org/uniprotkb/Q5VWN6) · Ensembl [ENSG00000108021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108021)

## Data

Gene col 2911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2911); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2911]; `tensor/DDL_lfc|DDL_z.npy` [2911]; `embed/gene_vectors.npy` [2911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2911 or target_col == 2911). Every well: [[TASOR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TASOR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
