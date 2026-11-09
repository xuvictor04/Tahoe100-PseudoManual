---
symbol: "ZNF10"
type: "gene"
col: 14982
ensembl_id: "ENSG00000256223"
name: "zinc finger protein 10"
location: "12q24.33"
module: 25
arm: "-"
pooled_cpm: 38.14
n_lines_expressing: 43
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ZNF10

*zinc finger protein 10* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.00× (z +23.4, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.435× (z -12.0, q 1e-30, down in 27 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.699× (z -5.2, q 3e-05, down in 22 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (J82 0.111×, A-427 0.176×, SNU-423 0.149×, SK-MEL-2 0.205×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW 900 0.139×, NCI-H460 0.207×, RKO 0.144×, SHP-77 0.205×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.147×, SW1417 0.193×, C32 0.204×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.313×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.496×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNNM4]] (+0.68, fdr 7e-06), [[CTR9]] (+0.67, fdr 1e-05), [[LIN7B]] (+0.61, fdr 6e-05); moves opposite to [[MOB1A]] (-0.67, fdr 1e-05), [[DR1]] (-0.64, fdr 3e-05), [[CERS2]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRAPPC2B]] → it (grade B ⚠); 4 go from it, the strongest it → [[C15orf61]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.00×** | +23.4 | 0e+00 | 38/41 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.94×** | +16.2 | 0e+00 | 41/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +16.1 | 0e+00 | 41/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +13.5 | 2e-39 | 39/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +10.1 | 5e-22 | 35/41 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +9.7 | 2e-20 | 31/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +9.2 | 4e-18 | 33/41 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +8.5 | 2e-15 | 34/40 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +7.1 | 9e-11 | 33/41 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +6.5 | 6e-09 | 29/41 (PANC-1, RKO, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +6.1 | 7e-08 | 28/41 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.7 | 7e-07 | 26/41 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +4.9 | 3e-05 | 21/41 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.80×** | +4.6 | 1e-04 | 22/41 (PANC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +4.6 | 2e-04 | 25/41 (HT-29, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 2e-04 | 25/41 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14982.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (J82 0.111×, A-427 0.176×, SNU-423 0.149×, SK-MEL-2 0.205×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW 900 0.139×, NCI-H460 0.207×, RKO 0.144×, SHP-77 0.205×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.147×, SW1417 0.193×, C32 0.204×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.313×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.496×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -12.0 | 1e-30 | 27/35 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.494×** | -10.6 | 1e-23 | 32/41 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.664×** | -5.7 | 2e-06 | 20/38 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -5.2 | 3e-05 | 22/40 (A-427, SW 1271, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.767×** | -3.8 | 0.015 | 15/40 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.6 | 0.030 | 19/41 (C32, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.6 | 6 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +20.9) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -17.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 55.1 | 7 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 52.2 | 7 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +19.0) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.496× (z -9.1) |
| [[A-427 (line)]] | wt | 65.4 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +21.1) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -10.8) |
| [[SW480 (line)]] | alt | 39.9 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +21.4) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 61.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +14.9) | — |
| [[A-172 (line)]] | wt | 21.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.54× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 20.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.30× (z +11.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 58.8 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -10.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 82.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -17.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 64.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 34.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +18.3) | — |
| [[C32 (line)]] | wt | 51.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 33.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +17.8) | — |
| [[J82 (line)]] | alt | 62.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 34.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 46.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 92.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -17.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 27.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -8.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 17.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.10× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 31.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +18.0) | — |
| [[HepG2_C3A (line)]] | wt | 67.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 44.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.74× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 27.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +18.6) | — |
| [[SNU-423 (line)]] | alt | 51.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -15.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 39.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +20.0) | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.101× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +10.9) | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0936× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 31.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -14.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 7 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM4]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CTR9]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.61 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[UBE2B]] | +0.60 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[AFMID]] | +0.60 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[SMIM26]] ⚠ | +0.59 | +0.42 / +0.54 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC00888-1]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[RPP21]] | +0.59 | +0.25 / +0.57 | both halves | 4e-04 |  |
| [[RNF113A]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[TPST1]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SUGP1]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[KRT10]] ⚠ | +0.58 | +0.30 / +0.63 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | +0.58 | +0.27 / +0.52 | both halves | 3e-04 |  |
| [[TRAPPC2B]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.67 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[DR1]] | -0.64 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[CERS2]] | -0.64 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[ERLIN2]] | -0.61 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[PSME3]] | -0.60 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[STMP1]] | -0.59 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[MSL3]] | -0.59 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[AIDA]] | -0.57 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ZMPSTE24]] | -0.57 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[CRPPA]] | -0.57 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[ELK4]] | -0.57 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[STX16]] | -0.56 | -0.42 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAPPC2B]] | B | TRAPPC2B activity raises ZNF10's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 3.46× lower at baseline in the lines without TRAPPC2B | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C15orf61]] | B | ZNF10 activity lowers C15orf61's level | lines that do not express ZNF10 (7) vs lines expressing it (43) | 1.89× higher at baseline in the lines without ZNF10 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |
| [[DCTN6-DT]] | B | ZNF10 activity lowers DCTN6-DT's level | lines that do not express ZNF10 (7) vs lines expressing it (43) | 1.67× higher at baseline in the lines without ZNF10 | 0.038 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |
| [[TRAPPC2B]] | B | ZNF10 activity raises TRAPPC2B's level | lines that do not express ZNF10 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without ZNF10 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |
| [[MAPKBP1]] | B | ZNF10 activity lowers MAPKBP1's level | lines that do not express ZNF10 (7) vs lines expressing it (43) | 1.22× higher at baseline in the lines without ZNF10 | 0.081 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.1, -28.5); signed map (-26.6, 13.2). **Vector** length 114, 32.6% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +23.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +0.9 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.1 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.1 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.1 | -12.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.9 | -10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:133,130,575-133,159,465 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P21506](https://www.uniprot.org/uniprotkb/P21506) (Zinc finger protein 10):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7556](https://www.ncbi.nlm.nih.gov/gene/7556):

> The protein encoded by this gene contains a C2H2 zinc finger, and has been shown to function as a transcriptional repressor. The Kruppel-associated box (KRAB) domain of this protein is found to be responsible for its transcriptional repression activity. RING finger containing protein TIF1 was reported to interact with the KRAB domain, and may serve as a mediator for the repression activity of this protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12879) · Entrez [7556](https://www.ncbi.nlm.nih.gov/gene/7556) · UniProt [P21506](https://www.uniprot.org/uniprotkb/P21506) · Ensembl [ENSG00000256223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256223)

## Data

Gene col 14982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14982); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14982]; `tensor/DDL_lfc|DDL_z.npy` [14982]; `embed/gene_vectors.npy` [14982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14982 or target_col == 14982). Every well: [[ZNF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
