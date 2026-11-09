---
symbol: "RALGAPA1"
type: "gene"
col: 10488
ensembl_id: "ENSG00000174373"
name: "Ral GTPase activating protein catalytic subunit alpha 1"
location: "14q13.2"
module: 11
arm: "+"
pooled_cpm: 170.47
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RALGAPA1

*Ral GTPase activating protein catalytic subunit alpha 1* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +20.6, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.502× (z -15.4, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.804× (z -6.9, q 6e-10, down in 27 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (A549 0.425×, LOX-IMVI 0.526×, A-427 0.482×, C-33 A 0.574×, …); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H23 0.250×, C-33 A 0.217×, NCI-H460 0.350×, SHP-77 0.302×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SK-MEL-2 0.202×, NCI-H460 0.328×, Panc 03.27 0.275×, MIA PaCa-2 0.281×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.461×, MIA PaCa-2 0.525×); [[Ponatinib (drug)]] 5 µM in 1 line (SW48 0.397×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK6]] (+0.60, fdr 2e-05), [[ZNF638]] (+0.60, fdr 1e-05), [[ZNF609]] (+0.60, fdr 3e-05); moves opposite to [[CCAR2]] (-0.60, fdr 1e-05), [[SDHAP4]] (-0.59, fdr 1e-05), [[SMPD4]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLXNB3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +20.6 | 0e+00 | 41/48 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.9 | 2e-16 | 34/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +6.6 | 6e-09 | 31/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +5.2 | 4e-05 | 27/48 (MIA PaCa-2, BT-474, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +4.8 | 2e-04 | 24/48 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 4e-04 | 24/48 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.5 | 5e-04 | 18/48 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.3 | 0.001 | 24/47 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.5 | 0.031 | 18/48 (CFPAC-1, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.031 | 20/49 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.031 | 16/47 (SW48, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.053 | 22/48 (BT-474, LS 180, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.15× | +3.1 | 0.083 | 17/49 (HOP62, SW 900, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.10 | 2/48 (HCT15, H4) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (A549 0.425×, LOX-IMVI 0.526×, A-427 0.482×, C-33 A 0.574×, …); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H23 0.250×, C-33 A 0.217×, NCI-H460 0.350×, SHP-77 0.302×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SK-MEL-2 0.202×, NCI-H460 0.328×, Panc 03.27 0.275×, MIA PaCa-2 0.281×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.461×, MIA PaCa-2 0.525×); [[Ponatinib (drug)]] 5 µM in 1 line (SW48 0.397×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.502×** | -15.4 | 0e+00 | 44/49 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.497×** | -14.5 | 3e-45 | 42/45 (SK-MEL-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -13.1 | 8e-37 | 41/44 (Panc 03.27, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.684×** | -8.5 | 2e-15 | 41/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.804×** | -6.9 | 6e-10 | 27/49 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -6.5 | 8e-09 | 36/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.9 | 7e-05 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.703×** | -4.1 | 0.003 | 20/38 (BT-474, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.855× | -3.5 | 0.029 | 22/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.873× | -3.0 | 0.13 | 14/47 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.868× | -3.0 | 0.13 | 14/48 (C-33 A, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 224 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 343 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.434× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 199 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -18.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 136 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +24.0) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.461× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 132 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +24.8) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 210 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -16.7) |
| [[HEC-1-A (line)]] | alt | 179 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.537× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 184 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 223 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 256 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -21.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 162 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -16.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 168 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -19.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 145 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 356 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.397× (z -10.1) |
| [[A-427 (line)]] | wt | 214 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.4) |
| [[BT-474 (line)]] | alt | 274 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +25.3) | — |
| [[C-33 A (line)]] | alt | 291 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -10.3) |
| [[C32 (line)]] | wt | 163 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 173 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 74.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +20.3) | — |
| [[LoVo (line)]] | wt | 151 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.572× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 267 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 241 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -21.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 224 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -18.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 176 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -8.5) |
| [[SW 900 (line)]] | alt | 138 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 55.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 141 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.499× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.483× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 129 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 188 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -9.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -15.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.2) | — |
| [[H4 (line)]] | wt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 84.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.4) | — |
| [[KATO III (line)]] | alt | 141 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 270 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.3) | — |
| [[NCI-H661 (line)]] | alt | 980 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.362× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -13.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 112 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0834× (z -10.1) |
| [[SW 1271 (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 227 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK6]] | +0.60 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[ZNF638]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZNF609]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[USP34]] | +0.59 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[DCTN6]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[NT5C]] | +0.58 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[NSRP1]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[JMJD1C]] | +0.56 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[TBRG1]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ATP9B]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TBCA]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[ZSCAN18]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCAR2]] | -0.60 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.59 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[SMPD4]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ZNF17]] | -0.57 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SDHA]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[TECR]] | -0.55 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[SNX33]] | -0.55 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[P3H1]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[RNF4]] | -0.53 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[DDOST]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ILF2]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNB3]] | B | PLXNB3 activity lowers RALGAPA1's level | lines that do not express PLXNB3 (10) vs lines expressing it (40) | 1.70× higher at baseline in the lines without PLXNB3 | 0.061 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.418). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.6, -13.2); signed map (7.5, -11.3). **Vector** length 106, 33.6% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +20.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +8.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.9 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -14.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -3.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.0 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | Ral GTPase activating protein catalytic subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.2 — chr14:35,538,352-35,809,304 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRIPE, DKFZp667F074, KIAA0884, Tulip1, RalGAPalpha1; previously GARNL1 |
| Reactome | 4 pathways, smallest: RHOH GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6GYQ0](https://www.uniprot.org/uniprotkb/Q6GYQ0) (Ral GTPase-activating protein subunit alpha-1):

> Catalytic subunit of the heterodimeric RalGAP1 complex which acts as a GTPase activator for the Ras-like small GTPases RALA and RALB.

**Summary**, from NCBI Gene [253959](https://www.ncbi.nlm.nih.gov/gene/253959):

> This gene encodes a major subunit of the RAL-GTPase activating protein. A similar protein in mouse binds E12, a transcriptional regulator of immunoglobulin genes. The mouse protein also functions in skeletal muscle by binding to the regulatory 14-3-3 proteins upon stimulation with insulin or muscle contraction. A pseudogene of this gene has been identified on chromosome 9. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:17770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17770) · Entrez [253959](https://www.ncbi.nlm.nih.gov/gene/253959) · UniProt [Q6GYQ0](https://www.uniprot.org/uniprotkb/Q6GYQ0) · Ensembl [ENSG00000174373](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174373)

## Data

Gene col 10488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10488); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10488]; `tensor/DDL_lfc|DDL_z.npy` [10488]; `embed/gene_vectors.npy` [10488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10488 or target_col == 10488). Every well: [[RALGAPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALGAPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
