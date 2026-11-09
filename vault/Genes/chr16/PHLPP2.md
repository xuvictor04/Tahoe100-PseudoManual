---
symbol: "PHLPP2"
type: "gene"
col: 465
ensembl_id: "ENSG00000040199"
name: "PH domain and leucine rich repeat protein phosphatase 2"
location: "16q22.2"
module: 57
arm: "-"
pooled_cpm: 54.07
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# PHLPP2

*PH domain and leucine rich repeat protein phosphatase 2* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.12× (z +21.8, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.426× (z -17.5, q 0e+00, down in 35 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.615× (z -5.2, q 3e-05, down in 24 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 0.0326×, LOX-IMVI 0.0472×, NCI-H460 0.129×, NCI-H1792 0.0675×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (C-33 A 0.0919×, A-172 0.192×, LOX-IMVI 0.141×, J82 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-172 0.170×, SK-MEL-2 0.0921×, A498 0.251×, PANC-1 0.282×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 0.05 µM in 1 line (SW 1271 0.0748×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HT-29 0.404×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HT-29 0.287×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLNRD1]] (+0.60, fdr 1e-05), [[DNMT3A]] (+0.59, fdr 1e-05), [[CRTC3]] (+0.59, fdr 2e-05); moves opposite to [[VAMP7]] (-0.56, fdr 5e-05), [[HLTF]] (-0.56, fdr 3e-05), [[LONP2]] (-0.54, fdr 4e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +21.8 | 0e+00 | 41/46 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +12.1 | 3e-31 | 34/46 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +11.1 | 1e-26 | 36/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +8.9 | 5e-17 | 34/46 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +8.8 | 2e-16 | 33/46 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +8.2 | 2e-14 | 32/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +6.3 | 3e-08 | 26/46 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.2 | 4e-08 | 27/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.2 | 5e-08 | 24/45 (BT-474, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.0 | 4e-05 | 18/46 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +4.8 | 8e-05 | 22/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.3 | 7e-04 | 21/46 (LS 180, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.003 | 18/46 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +3.9 | 0.003 | 19/46 (SW480, RPMI-7951, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.006 | 14/46 (RKO, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.010 | 16/46 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.016 | 6/46 (SW1417, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 465.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 0.0326×, LOX-IMVI 0.0472×, NCI-H460 0.129×, NCI-H1792 0.0675×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (C-33 A 0.0919×, A-172 0.192×, LOX-IMVI 0.141×, J82 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-172 0.170×, SK-MEL-2 0.0921×, A498 0.251×, PANC-1 0.282×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 0.05 µM in 1 line (SW 1271 0.0748×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HT-29 0.404×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HT-29 0.287×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.426×** | -17.5 | 0e+00 | 35/46 (A-172, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.436×** | -15.7 | 0e+00 | 34/43 (C-33 A, A-172, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.471×** | -14.8 | 0e+00 | 30/40 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.615×** | -5.2 | 3e-05 | 24/45 (SNU-1, H4, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 0.753× | -3.0 | 0.19 | 15/44 (NCI-H661, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.846× | -3.0 | 0.19 | 10/46 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.862× | -3.0 | 0.19 | 6/46 (AN3 CA, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.0 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -22.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 135 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.404× (z -9.7) |
| [[A498 (line)]] | wt | 60.6 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -15.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 76.4 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 89.3 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -14.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 80.0 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 35.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.0675× (z -21.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 44.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -14.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 52.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 95.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0326× (z -38.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 98.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0919× (z -21.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 61.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 67.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 47.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.0472× (z -25.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 38.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -11.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 49.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -9.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 41.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -11.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 41.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -13.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 27.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 52.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 90.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 53.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0921× (z -20.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 64.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 70.6 | 0 | 1 | — | [[Verteporfin (drug)]] 0.05 µM 0.0748× (z -9.7) |
| [[SW 900 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 97.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[DNMT3A]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CRTC3]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RIMKLB]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[FAM171A1]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ATXN2]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[HIVEP1]] | +0.53 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[MSX1]] | +0.53 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[ZBTB8A]] | +0.52 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[WTIP]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[ZBTB7A]] | +0.52 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[CDR2]] | +0.51 | +0.47 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP7]] | -0.56 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[HLTF]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LONP2]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[UBE4A]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SNRNP200]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[GUSBP1]] | -0.50 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[MORF4L1]] | -0.49 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[RTF2]] | -0.48 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[GSTM4]] | -0.48 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[PLA2G12A]] | -0.48 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CYB5R4]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[COPS7A]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.6, 12.6); signed map (8.5, -5.1). **Vector** length 99.9, 25.3% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +21.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +3.7 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +8.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +5.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +2.0 |
|  | [[NG25 (drug)]] 5 µM |  | -4.2 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PH domain and leucine rich repeat protein phosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,637,835-71,724,701 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0931, PPM3B; previously PHLPPL |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Protein phosphatases, Mg2+/Mn2+ dependent; Small nucleolar RNA protein coding host genes |
| Reactome | 3 pathways, smallest: Negative regulation of the PI3K/AKT network; PIP3 activates AKT signaling; Intracellular signaling by second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZVD8](https://www.uniprot.org/uniprotkb/Q6ZVD8) (PH domain leucine-rich repeat-containing protein phosphatase 2):

> Protein phosphatase involved in regulation of Akt and PKC signaling. Mediates dephosphorylation in the C-terminal domain hydrophobic motif of members of the AGC Ser/Thr protein kinase family; specifically acts on 'Ser-473' of AKT1, 'Ser-660' of PRKCB isoform beta-II and 'Ser-657' of PRKCA. Akt regulates the balance between cell survival and apoptosis through a cascade that primarily alters the function of transcription factors that regulate pro- and antiapoptotic genes. Dephosphorylation of …

**Summary**, from NCBI Gene [23035](https://www.ncbi.nlm.nih.gov/gene/23035):

> Predicted to enable metal ion binding activity and protein serine/threonine phosphatase activity. Predicted to be involved in intracellular signal transduction. Located in cytosol and intercellular bridge. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29149) · Entrez [23035](https://www.ncbi.nlm.nih.gov/gene/23035) · UniProt [Q6ZVD8](https://www.uniprot.org/uniprotkb/Q6ZVD8) · Ensembl [ENSG00000040199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040199)

## Data

Gene col 465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 465); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 465]; `tensor/DDL_lfc|DDL_z.npy` [465]; `embed/gene_vectors.npy` [465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 465 or target_col == 465). Every well: [[PHLPP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHLPP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
