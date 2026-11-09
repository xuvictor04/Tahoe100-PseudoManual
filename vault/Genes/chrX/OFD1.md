---
symbol: "OFD1"
type: "gene"
col: 505
ensembl_id: "ENSG00000046651"
name: "OFD1 centriole and centriolar satellite protein"
location: "Xp22.2"
module: 20
arm: "-"
pooled_cpm: 131.34
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# OFD1

*OFD1 centriole and centriolar satellite protein* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +25.1, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.590× (z -12.1, q 1e-30, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.615× (z -6.0, q 2e-07, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A549 0.210×, A-427 0.238×, NCI-H1573 0.240×, NCI-H23 0.294×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 0.286×, SW480 0.384×, NCI-H1573 0.252×, SNU-423 0.381×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A549 0.227×, NCI-H1792 0.297×, SNU-423 0.388×; ⚠ toxic; transcription drop); [[Voriconazole (drug)]] 0.05 µM in 1 line (SW 1088 0.0633×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1573 0.479×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BOLA1]] (+0.67, fdr 7e-06), [[RSF1]] (+0.67, fdr 7e-06), [[WASHC1]] (+0.66, fdr 7e-06); moves opposite to [[MAPK9]] (-0.70, fdr 7e-06), [[GPD1L]] (-0.70, fdr 7e-06), [[GOT2]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +25.1 | 0e+00 | 45/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +11.0 | 1e-25 | 37/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +10.0 | 3e-21 | 37/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.8 | 2e-04 | 19/49 (RKO, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.8 | 0.016 | 0/50 | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.087 | 9/48 (CFPAC-1, SNU-423, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 505.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A549 0.210×, A-427 0.238×, NCI-H1573 0.240×, NCI-H23 0.294×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 0.286×, SW480 0.384×, NCI-H1573 0.252×, SNU-423 0.381×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A549 0.227×, NCI-H1792 0.297×, SNU-423 0.388×; ⚠ toxic; transcription drop); [[Voriconazole (drug)]] 0.05 µM in 1 line (SW 1088 0.0633×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1573 0.479×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -12.1 | 1e-30 | 31/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -9.7 | 5e-20 | 34/45 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.675×** | -9.3 | 2e-18 | 35/49 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -7.5 | 7e-12 | 33/47 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.615×** | -6.0 | 2e-07 | 36/48 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.811×** | -5.0 | 6e-05 | 23/48 (A549, RPMI-7951, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.683×** | -4.7 | 2e-04 | 19/38 (SK-MEL-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.826×** | -4.5 | 4e-04 | 23/48 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.828×** | -4.5 | 4e-04 | 22/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.822×** | -4.5 | 4e-04 | 23/47 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.839× | -4.2 | 0.002 | 21/48 (HEC-1-A, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.841× | -4.1 | 0.002 | 20/48 (LoVo, COLO 205, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.856× | -3.7 | 0.010 | 17/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 0.865× | -3.4 | 0.023 | 23/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.909× | -3.2 | 0.049 | 5/48 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.783×** | -3.0 | 0.076 | 14/48 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.882× | -3.0 | 0.082 | 18/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.879× | -3.0 | 0.082 | 10/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.879× | -2.9 | 0.082 | 15/48 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.882× | -2.9 | 0.100 | 10/48 (SK-MEL-2, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 343 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.479× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 122 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 119 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 127 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +18.3) | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -12.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 96.6 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.520× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 102 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 156 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.473× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 214 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 282 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 180 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -14.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 202 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -17.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 113 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +29.0) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -18.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 152 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.398× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 190 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -12.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 124 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -9.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 114 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 164 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.9) | — |
| [[LS 180 (line)]] | wt | 91.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.5) | — |
| [[NCI-H2347 (line)]] | alt | 116 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +24.5) | — |
| [[SK-MEL-2 (line)]] | alt | 85.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 138 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +18.0) | — |
| [[A498 (line)]] | wt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +16.7) | — |
| [[A549 (line)]] | wt | 164 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 76.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +24.1) | — |
| [[COLO 205 (line)]] | alt | 201 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.478× (z -8.7) ⚠ toxic |
| [[H4 (line)]] | wt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 180 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +23.2) | — |
| [[NCI-H23 (line)]] | alt | 96.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 91.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.7) | — |
| [[SW 900 (line)]] | alt | 63.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +17.2) | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 136 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 64.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 73.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.9) | — |
| [[J82 (line)]] | alt | 82.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 71.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 173 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 153 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.4) | — |
| [[RKO (line)]] | wt | 104 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 99.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.3) | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 1 | — | [[Voriconazole (drug)]] 0.05 µM 0.0633× (z -11.1) |
| [[AN3 CA (line)]] | alt | 143 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 94.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BOLA1]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[RSF1]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ZKSCAN1]] | +0.65 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[CHMP4A]] | +0.65 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[EIF4EBP3]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[METTL23]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[LRCH3]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.64 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.70 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[GPD1L]] | -0.70 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[GOT2]] | -0.69 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[SKP2]] | -0.69 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[ANKRD52]] | -0.68 | -0.70 / -0.66 | both halves | 7e-06 |  |
| [[TBC1D24]] | -0.67 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[HACD3]] | -0.67 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[NUP93]] | -0.67 | -0.73 / -0.60 | both halves | 7e-06 |  |
| [[FAR1]] | -0.67 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[PPT1]] | -0.67 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[TMEM109]] | -0.66 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[RPSA]] | -0.66 | -0.62 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.2, -27.8); signed map (-4.5, 2.9). **Vector** length 132, 39.3% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +13.4 | +25.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +4.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.0 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +0.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +2.7 | +2.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -5.3 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -12.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Erlotinib (drug)]] 5 µM |  | -2.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | OFD1 centriole and centriolar satellite protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:13,734,743-13,777,955 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 71-7A, JBTS10; previously CXorf5, RP23 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Reactome | 19 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75665](https://www.uniprot.org/uniprotkb/O75665) (Centriole and centriolar satellite protein OFD1):

> Component of the centrioles controlling mother and daughter centrioles length. Recruits to the centriole IFT88 and centriole distal appendage-specific proteins including CEP164 (By similarity). Involved in the biogenesis of the cilium, a centriole-associated function. The cilium is a cell surface projection found in many vertebrate cells required to transduce signals important for development and tissue homeostasis. Plays an important role in development by regulating Wnt signaling and the …

**Summary**, from NCBI Gene [8481](https://www.ncbi.nlm.nih.gov/gene/8481):

> This gene is located on the X chromosome and encodes a centrosomal protein. A knockout mouse model has been used to study the effect of mutations in this gene. The mouse gene is also located on the X chromosome, however, unlike the human gene it is not subject to X inactivation. Mutations in this gene are associated with oral-facial-digital syndrome type I and Simpson-Golabi-Behmel syndrome type 2. Many pseudogenes have been identified; a single pseudogene is found on chromosome 5 while as many …

**Accessions** — [HGNC:2567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2567) · Entrez [8481](https://www.ncbi.nlm.nih.gov/gene/8481) · UniProt [O75665](https://www.uniprot.org/uniprotkb/O75665) · Ensembl [ENSG00000046651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000046651)

## Data

Gene col 505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 505); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 505]; `tensor/DDL_lfc|DDL_z.npy` [505]; `embed/gene_vectors.npy` [505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 505 or target_col == 505). Every well: [[OFD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OFD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
