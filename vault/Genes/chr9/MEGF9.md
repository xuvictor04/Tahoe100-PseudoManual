---
symbol: "MEGF9"
type: "gene"
col: 2804
ensembl_id: "ENSG00000106780"
name: "multiple EGF like domains 9"
location: "9q33.2"
module: 85
arm: "+"
pooled_cpm: 40.34
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# MEGF9

*multiple EGF like domains 9* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.20× (z +36.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.697× (z -9.0, q 2e-16, down in 24 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.850× (z -4.2, q 0.003, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.113×, A549 0.264×, SHP-77 0.200×, Panc 03.27 0.340×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H2030 0.175×, C-33 A 0.198×, KATO III 0.292×, NCI-H460 0.359×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.393×, SHP-77 0.233×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.312×, A-172 0.504×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.312×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GAS2L1]] (+0.57, fdr 4e-04), [[MAGI3]] (+0.56, fdr 1e-05), [[BTBD3]] (+0.55, fdr 2e-04); moves opposite to [[KRR1]] (-0.62, fdr 3e-04), [[GLIPR1-AS1]] (-0.58, fdr 2e-04), [[ZNF621]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.20×** | +36.8 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.85×** | +34.5 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.80×** | +34.2 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.78×** | +26.2 | 0e+00 | 48/48 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.30×** | +21.3 | 0e+00 | 46/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.54×** | +16.9 | 0e+00 | 45/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +14.8 | 0e+00 | 41/48 (A-172, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +14.6 | 0e+00 | 32/48 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +11.3 | 7e-28 | 31/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +9.9 | 4e-21 | 36/48 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +9.3 | 5e-19 | 32/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.38×** | +7.8 | 2e-13 | 28/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +7.1 | 6e-11 | 26/48 (LoVo, KATO III, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +6.9 | 2e-10 | 24/47 (LS 180, RKO, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.58×** | +6.1 | 4e-08 | 18/48 (RKO, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +5.9 | 1e-07 | 13/48 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +5.7 | 4e-07 | 22/48 (A498, C32, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +5.4 | 2e-06 | 17/47 (NCI-H460, BT-474, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +5.3 | 3e-06 | 16/49 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2804.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.113×, A549 0.264×, SHP-77 0.200×, Panc 03.27 0.340×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H2030 0.175×, C-33 A 0.198×, KATO III 0.292×, NCI-H460 0.359×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.393×, SHP-77 0.233×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.312×, A-172 0.504×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.312×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -9.0 | 2e-16 | 24/37 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.784×** | -5.8 | 2e-06 | 17/41 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -4.2 | 0.003 | 17/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -4.2 | 0.003 | 16/47 (CHP-212, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.894× | -4.2 | 0.003 | 11/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.735×** | -4.2 | 0.003 | 11/48 (PANC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.852× | -4.2 | 0.003 | 14/47 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.858× | -4.0 | 0.005 | 16/48 (HEC-1-A, SW1417, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.859× | -4.0 | 0.005 | 14/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.864× | -3.8 | 0.008 | 11/48 (HT-29, LoVo, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.868× | -3.7 | 0.011 | 13/48 (HEC-1-A, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.868× | -3.7 | 0.011 | 21/45 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.910× | -3.5 | 0.020 | 13/48 (CHP-212, SW 1271, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.881× | -3.3 | 0.039 | 16/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.883× | -3.1 | 0.068 | 10/48 (NCI-H460, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 34.1 | 9 (3 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.30× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -22.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.0 | 7 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.74× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 118 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 31.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.7) | — |
| [[SW480 (line)]] | alt | 47.0 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +15.8) | — |
| [[A498 (line)]] | wt | 70.4 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 42.7 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.13× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -10.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 44.7 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.46× (z +13.9) | — |
| [[A-172 (line)]] | wt | 47.3 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 3.70× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.8) |
| [[A549 (line)]] | wt | 48.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.97× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 35.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 20.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.51× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 39.3 | 4 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.85× (z +11.9) | [[Lonafarnib (drug)]] 5 µM 0.144× (z -9.1) ⚠ toxic |
| [[J82 (line)]] | alt | 44.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 32.9 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.72× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.58× (z +17.4) | — |
| [[C32 (line)]] | wt | 28.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 31.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 28.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.66× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 58.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.05× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 37.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 36.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.76× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 38.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 51.7 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.77× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 42.4 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -11.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.93× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 47.1 | 4 | 0 | [[Belinostat (drug)]] 5 µM 4.18× (z +13.3) | — |
| [[A-427 (line)]] | wt | 21.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.40× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +10.5) | — |
| [[H4 (line)]] | wt | 25.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.60× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.13× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.6× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 37.7 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.52× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 34.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 43.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.54× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 45.5 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.25× (z +8.7) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.312× (z -8.7) |
| [[HS-578T (line)]] | alt | 16.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.09× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.2) |
| [[BT-474 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAS2L1]] | +0.57 | +0.26 / +0.43 | both halves | 4e-04 |  |
| [[MAGI3]] | +0.56 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[BTBD3]] | +0.55 | +0.32 / +0.37 | both halves | 2e-04 |  |
| [[RANBP9]] | +0.55 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[NMT2]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[STK38]] | +0.54 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[CYTH3]] | +0.54 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[SORT1]] | +0.54 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CFD]] | +0.54 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[PEDS1]] | +0.53 | +0.25 / +0.47 | both halves | 4e-04 |  |
| [[CRIP2]] | +0.53 | +0.35 / +0.35 | both halves | 1e-04 |  |
| [[HMGN3]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRR1]] | -0.62 | -0.29 / -0.64 | both halves | 3e-04 |  |
| [[GLIPR1-AS1]] | -0.58 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ZNF621]] | -0.58 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[ALG13]] | -0.56 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.56 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[CSTF3]] | -0.56 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[EMG1]] | -0.56 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[DPH2]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ACAD9]] | -0.54 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[CYP27B1]] | -0.54 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[C8orf33]] | -0.54 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[ZFHX2-AS1]] | -0.54 | -0.14 / -0.41 | ⚠ not reproduced | 0.002 |  |
| [[DHX34]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MEGF9's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (8.8, 7.0); signed map (-19.0, 22.3). **Vector** length 83.3, 19.0% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +26.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +21.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.6 | +16.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +14.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +9.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +9.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | +5.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.6 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | multiple EGF like domains 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:120,600,811-120,714,470 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EGFL5 |
| Matched by | ensembl_id |

UniProt [Q9H1U4](https://www.uniprot.org/uniprotkb/Q9H1U4) carries no function annotation.

**Summary**, from NCBI Gene [1955](https://www.ncbi.nlm.nih.gov/gene/1955):

> Predicted to be located in basement membrane and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3234) · Entrez [1955](https://www.ncbi.nlm.nih.gov/gene/1955) · UniProt [Q9H1U4](https://www.uniprot.org/uniprotkb/Q9H1U4) · Ensembl [ENSG00000106780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106780)

## Data

Gene col 2804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2804); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2804]; `tensor/DDL_lfc|DDL_z.npy` [2804]; `embed/gene_vectors.npy` [2804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2804 or target_col == 2804). Every well: [[MEGF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEGF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
