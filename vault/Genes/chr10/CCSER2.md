---
symbol: "CCSER2"
type: "gene"
col: 2877
ensembl_id: "ENSG00000107771"
name: "coiled-coil serine rich protein 2"
location: "10q23.1"
module: 65
arm: "-"
pooled_cpm: 123.81
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# CCSER2

*coiled-coil serine rich protein 2* — 10q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +12.6, q 2e-33, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.595× (z -12.9, q 3e-35, down in 43 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.702× (z -8.8, q 2e-16, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-172 0.348×, NCI-H1573 0.322×, HEC-1-A 0.306×, LOX-IMVI 0.308×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.335×, RKO 0.281×, NCI-H460 0.374×, A-172 0.435×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-423 0.292×, A-172 0.362×, SHP-77 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 3 lines (A-172 0.566×, HOP62 0.603×, SNU-1 0.494×); [[Auranofin (drug)]] 5 µM in 3 lines (SW480 0.519×, SHP-77 0.374×, HEC-1-A 0.557×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.556×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERC1]] (+0.62, fdr 1e-05), [[DCTN2]] (+0.59, fdr 1e-05), [[EXOC6B]] (+0.59, fdr 2e-05); moves opposite to [[SMPD4]] (-0.49, fdr 3e-05), [[COPS8-DT]] (-0.48, fdr 1e-04), [[RHOXF1]] (-0.48, fdr 3e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +12.6 | 2e-33 | 34/48 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +11.9 | 3e-30 | 44/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +11.0 | 1e-25 | 42/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +8.9 | 6e-17 | 39/48 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +8.8 | 2e-16 | 36/48 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +8.6 | 6e-16 | 35/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +8.2 | 3e-14 | 35/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.8 | 4e-13 | 28/48 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +6.9 | 3e-10 | 36/47 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +6.2 | 4e-08 | 35/49 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +5.8 | 3e-07 | 17/48 (HT-29, KATO III, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +5.5 | 2e-06 | 16/48 (SK-MEL-2, SW48, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +5.3 | 6e-06 | 34/49 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 1e-04 | 28/47 (SNU-423, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.2 | 0.001 | 19/48 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.9 | 0.003 | 9/48 (HT-29, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2877.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-172 0.348×, NCI-H1573 0.322×, HEC-1-A 0.306×, LOX-IMVI 0.308×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.335×, RKO 0.281×, NCI-H460 0.374×, A-172 0.435×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-423 0.292×, A-172 0.362×, SHP-77 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 3 lines (A-172 0.566×, HOP62 0.603×, SNU-1 0.494×); [[Auranofin (drug)]] 5 µM in 3 lines (SW480 0.519×, SHP-77 0.374×, HEC-1-A 0.557×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.556×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.595×** | -12.9 | 3e-35 | 43/49 (A-427, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.632×** | -11.0 | 2e-25 | 32/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.646×** | -10.8 | 4e-25 | 41/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -8.8 | 2e-16 | 35/48 (SW480, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.681×** | -8.1 | 8e-14 | 32/45 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.764×** | -6.7 | 2e-09 | 30/48 (LS 180, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.632×** | -5.9 | 3e-07 | 31/49 (PANC-1, NCI-H1792, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.815×** | -5.1 | 3e-05 | 25/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.836× | -4.3 | 0.001 | 21/47 (MIA PaCa-2, hTERT-HPNE, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | 0.849× | -4.1 | 0.003 | 19/48 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -3.6 | 0.017 | 0/50 | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.908× | -3.4 | 0.032 | 4/48 (LoVo, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.877× | -3.3 | 0.047 | 20/48 (SW480, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 139 | 4 | 7 (7 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.26× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 262 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.566× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 130 | 4 (1 ⚠) | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.42× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 142 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.420× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.519× (z -10.7) |
| [[C32 (line)]] | wt | 133 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 165 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.533× (z -8.5) |
| [[LS 180 (line)]] | wt | 124 | 1 | 5 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.16× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -15.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H1573 (line)]] | alt | 131 | 3 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.79× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 162 | 1 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.73× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.427× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.336× (z -9.6) |
| [[HOP62 (line)]] | alt | 151 | 1 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.92× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.409× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.603× (z -9.5) |
| [[A498 (line)]] | wt | 81.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.95× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 259 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 88.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +19.9) | — |
| [[HEC-1-A (line)]] | alt | 96.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.557× (z -8.9) |
| [[LoVo (line)]] | wt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 89.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -10.3) |
| [[SNU-1 (line)]] | wt | 193 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.494× (z -9.3) |
| [[C-33 A (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 150 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 169 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.1) | — |
| [[J82 (line)]] | alt | 74.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.406× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 118 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.250× (z -8.5) |
| [[SHP-77 (line)]] | alt | 86.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.374× (z -9.2) |
| [[SNU-423 (line)]] | alt | 216 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 51.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +16.0) | — |
| [[SW1417 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.464× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 63.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.1) | — |
| [[H4 (line)]] | wt | 152 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.7) | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.427× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 96.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.394× (z -12.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RPMI-7951 (line)]] | alt | 96.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 186 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.0) | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.118× (z -8.5) |
| [[BT-474 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERC1]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[DCTN2]] | +0.59 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[EXOC6B]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[FSD1L]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[KIF1B]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[FER]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GLRX2]] | +0.56 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[GAB2]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PSMA7]] | +0.53 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[CLIP1]] | +0.53 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[SPIRE1]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[PRMT2]] | +0.51 | +0.48 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPD4]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[COPS8-DT]] | -0.48 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[RHOXF1]] | -0.48 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[PRPF38A]] | -0.47 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[HNMT]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ZNF141]] | -0.45 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[GANAB]] | -0.45 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[TPCN1]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[DIDO1]] | -0.45 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[SNRPG]] | -0.45 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[HOXA3]] | -0.45 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[GRK2]] | -0.44 | -0.46 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.162). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.7, -1.8); signed map (-21.7, -6.6). **Vector** length 110, 32.8% of its response variance represented; |z| ≥ 3 in 1,308 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.1 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.1 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +8.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.2 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +12.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.5 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.2 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +3.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -8.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -5.2 | -10.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.6 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil serine rich protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.1 — chr10:84,328,586-84,518,521 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1128, FAM190B |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7U1](https://www.uniprot.org/uniprotkb/Q9H7U1) (Serine-rich coiled-coil domain-containing protein 2):

> Microtubule-binding protein which might play a role in microtubule bundling.

**Summary**, from NCBI Gene [54462](https://www.ncbi.nlm.nih.gov/gene/54462):

> Predicted to enable microtubule binding activity. Predicted to be involved in microtubule bundle formation. Predicted to be located in cytoskeleton. Predicted to be active in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29197) · Entrez [54462](https://www.ncbi.nlm.nih.gov/gene/54462) · UniProt [Q9H7U1](https://www.uniprot.org/uniprotkb/Q9H7U1) · Ensembl [ENSG00000107771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107771)

## Data

Gene col 2877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2877); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2877]; `tensor/DDL_lfc|DDL_z.npy` [2877]; `embed/gene_vectors.npy` [2877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2877 or target_col == 2877). Every well: [[CCSER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCSER2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
