---
symbol: "SEPTIN2"
type: "gene"
col: 9637
ensembl_id: "ENSG00000168385"
name: "septin 2"
location: "2q37.3"
module: 7
arm: "-"
pooled_cpm: 268.05
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SEPTIN2

*septin 2* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.88× (z +15.5, q 0e+00, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 2.35×, PANC-1 2.29×, NCI-H460 2.17×, Panc 03.27 2.76×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H460 2.37×, HEC-1-A 2.12×, NCI-H2030 2.22×, PANC-1 2.09×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.05×; ⚠ cell-cycle shift, explains ~25% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.781× (z -6.3, q 2e-07, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HOP62 0.507×, HS-578T 0.555×, NCI-H1792 0.579×, CFPAC-1 0.685×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (HOP62 0.505×, HS-578T 0.472×, RPMI-7951 0.517×, J82 0.598×, …); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HOP62 0.587×; ⚠ cell-cycle shift, explains ~35% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (BT-474 0.513×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC3]] (+0.66, fdr 1e-05), [[NKTR]] (+0.65, fdr 7e-06), [[CA5B]] (+0.63, fdr 7e-06); moves opposite to [[JAGN1]] (-0.69, fdr 7e-06), [[DDX28]] (-0.66, fdr 1e-05), [[TP53RK]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9637.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 2.35×, PANC-1 2.29×, NCI-H460 2.17×, Panc 03.27 2.76×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H460 2.37×, HEC-1-A 2.12×, NCI-H2030 2.22×, PANC-1 2.09×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.05×; ⚠ cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +15.5 | 0e+00 | 42/44 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +15.3 | 0e+00 | 46/49 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +7.1 | 2e-10 | 32/45 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.27×** | +6.0 | 2e-07 | 27/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.21×** | +4.7 | 3e-04 | 25/47 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | 1.19× | +4.4 | 9e-04 | 22/48 (PANC-1, SW480, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.8 | 0.013 | 20/38 (HEC-1-A, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.035 | 6/48 (NCI-H23, Hs 766T, …) | rises with dose | plate-row cell shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.28×** | +3.3 | 0.058 | 24/47 (H4, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.058 | 17/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.14 | 6/49 (CFPAC-1, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9637.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HOP62 0.507×, HS-578T 0.555×, NCI-H1792 0.579×, CFPAC-1 0.685×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (HOP62 0.505×, HS-578T 0.472×, RPMI-7951 0.517×, J82 0.598×, …); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HOP62 0.587×; ⚠ cell-cycle shift, explains ~35% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (BT-474 0.513×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.781×** | -6.3 | 2e-07 | 31/48 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.844× | -6.1 | 3e-07 | 25/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -4.6 | 7e-04 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.838× | -4.5 | 9e-04 | 23/48 (HOP62, NCI-H2347, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.862× | -3.8 | 0.016 | 20/48 (H4, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.863× | -3.8 | 0.016 | 16/48 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.866× | -3.7 | 0.020 | 20/48 (HS-578T, NCI-H1573, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.869× | -3.6 | 0.026 | 11/48 (SW48, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.906× | -3.5 | 0.026 | 7/48 (J82, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.873× | -3.5 | 0.031 | 18/48 (HOP62, H4, …) | rises with dose |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.875× | -3.4 | 0.036 | 7/48 (NCI-H1792, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.886× | -3.1 | 0.10 | 8/49 (A-172, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 355 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.98× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.505× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 214 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +13.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 276 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +15.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 311 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -10.9) |
| [[LoVo (line)]] | wt | 238 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 358 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +11.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 233 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 299 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +14.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 291 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +12.8) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[HEC-1-A (line)]] | alt | 270 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +16.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 201 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.598× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 346 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 218 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +14.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 222 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 350 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 308 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.71× (z +10.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +10.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 180 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 181 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +13.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 358 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 251 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +17.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 196 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +14.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 223 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SNU-1 (line)]] | wt | 243 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 237 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 288 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.87× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.551× (z -8.5) |
| [[AN3 CA (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +8.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 181 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.513× (z -8.9) |
| [[C32 (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.0) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 350 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -8.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[hTERT-HPNE (line)]] | wt | 338 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.513× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 454 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[RPMI-7951 (line)]] | alt | 398 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.517× (z -10.5) |
| [[SHP-77 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.79× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 259 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.73× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 217 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.65× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 360 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 258 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 348 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 286 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 266 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 213 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 402 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 205 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC3]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[NKTR]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CA5B]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[HDAC6]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[USP48]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[SEC31A]] | +0.62 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.60 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[COPA]] | +0.60 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[SEC63]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NUCB2]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[COPG1]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAGN1]] | -0.69 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[DDX28]] | -0.66 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[TP53RK]] | -0.65 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[YTHDF2]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[HPS6]] | -0.63 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[TOE1]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TRMT10C]] | -0.61 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[FADD]] | -0.60 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[NIP7]] | -0.59 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[MRM3]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ZNF629]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.58 | -0.71 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-40.0, 9.6); signed map (-58.0, 6.7). **Vector** length 136, 43.7% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.0 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +15.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.7 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.8 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.4 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | septin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,315,100-241,354,027 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0158, hNedd5, Pnutl3, Septin-2; previously DIFF6, NEDD5, SEPT2 |
| Gene groups (HGNC) | Septins |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15019](https://www.uniprot.org/uniprotkb/Q15019) (Septin-2):

> Filament-forming cytoskeletal GTPase. Forms a filamentous structure with SEPTIN12, SEPTIN6, SEPTIN2 and probably SEPTIN4 at the sperm annulus which is required for the structural integrity and motility of the sperm tail during postmeiotic differentiation. Required for normal organization of the actin cytoskeleton. Plays a role in the biogenesis of polarized columnar-shaped epithelium by maintaining polyglutamylated microtubules, thus facilitating efficient vesicle transport, and by impeding …

**Summary**, from NCBI Gene [4735](https://www.ncbi.nlm.nih.gov/gene/4735):

> Enables identical protein binding activity. Involved in cytoskeleton organization. Located in several cellular components, including cytoskeleton; photoreceptor connecting cilium; and sperm annulus. Part of septin complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7729) · Entrez [4735](https://www.ncbi.nlm.nih.gov/gene/4735) · UniProt [Q15019](https://www.uniprot.org/uniprotkb/Q15019) · Ensembl [ENSG00000168385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168385)

## Data

Gene col 9637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9637); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9637]; `tensor/DDL_lfc|DDL_z.npy` [9637]; `embed/gene_vectors.npy` [9637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9637 or target_col == 9637). Every well: [[SEPTIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
