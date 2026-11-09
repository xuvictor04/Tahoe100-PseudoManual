---
symbol: "EXOC1"
type: "gene"
col: 1647
ensembl_id: "ENSG00000090989"
name: "exocyst complex component 1"
location: "4q12"
module: 5
arm: "-"
pooled_cpm: 116.03
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# EXOC1

*exocyst complex component 1* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.61× (z +5.5, q 3e-05, up in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (RKO 3.34×, NCI-H2030 2.52×, NCI-H23 2.09×, NCI-H460 1.88×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (NCI-H460 2.23×, RKO 3.30×, NCI-H2030 2.60×, A498 2.09×; ⚠ cell-cycle shift, explains ~14% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (BT-474 2.41×, NCI-H2030 1.86×, SW1417 1.67×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 2 lines (NCI-H460 1.96×, A-427 2.11×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.503× (z -15.0, q 0e+00, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.817× (z -4.4, q 9e-04, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (CFPAC-1 0.290×, Panc 03.27 0.274×, NCI-H1792 0.297×, SW480 0.332×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (AsPC-1 0.343×, CFPAC-1 0.373×, SHP-77 0.362×, NCI-H1792 0.368×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A549 0.225×, CFPAC-1 0.296×, Panc 03.27 0.322×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.542×); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.0861×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.540×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA7]] (+0.71, fdr 7e-06), [[HADHB]] (+0.70, fdr 8e-06), [[MRPS31]] (+0.69, fdr 7e-06); moves opposite to [[HNRNPAB]] (-0.66, fdr 7e-06), [[TFDP1]] (-0.64, fdr 7e-06), [[MACROH2A1]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1647.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (RKO 3.34×, NCI-H2030 2.52×, NCI-H23 2.09×, NCI-H460 1.88×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (NCI-H460 2.23×, RKO 3.30×, NCI-H2030 2.60×, A498 2.09×; ⚠ cell-cycle shift, explains ~14% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (BT-474 2.41×, NCI-H2030 1.86×, SW1417 1.67×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 2 lines (NCI-H460 1.96×, A-427 2.11×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.61×** | +5.5 | 3e-05 | 38/49 (A-427, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.59×** | +5.3 | 3e-05 | 35/47 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.9 | 2e-04 | 23/48 (RKO, NCI-H2030, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.3 | 0.002 | 19/49 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +4.2 | 0.003 | 24/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.010 | 8/48 (BT-474, SW 900, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.015 | 22/49 (A-427, HepG2/C3A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.5 | 0.033 | 6/48 (C32, A-427, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.11× | +3.3 | 0.052 | 5/48 (SHP-77, BT-474, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.12 | 7/48 (BT-474, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.15× | +3.0 | 0.12 | 12/48 (NCI-H2030, LoVo, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1647.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (CFPAC-1 0.290×, Panc 03.27 0.274×, NCI-H1792 0.297×, SW480 0.332×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (AsPC-1 0.343×, CFPAC-1 0.373×, SHP-77 0.362×, NCI-H1792 0.368×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A549 0.225×, CFPAC-1 0.296×, Panc 03.27 0.322×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H460 0.542×); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.0861×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.540×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.503×** | -15.0 | 0e+00 | 41/49 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -13.3 | 5e-38 | 37/44 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.610×** | -10.0 | 3e-21 | 39/45 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.700×** | -7.8 | 1e-12 | 39/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -7.4 | 2e-11 | 33/47 (CFPAC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.814×** | -4.5 | 7e-04 | 24/48 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -4.4 | 9e-04 | 24/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | 0.833× | -4.0 | 0.005 | 23/48 (HCT15, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.835× | -3.9 | 0.005 | 19/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.727×** | -3.6 | 0.016 | 20/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.864× | -3.1 | 0.11 | 9/48 (NCI-H2030, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.905× | -3.0 | 0.11 | 12/48 (CFPAC-1, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 145 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.540× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 115 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.96× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.542× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 136 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -15.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 155 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -15.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 71.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.11× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 57.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 110 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -10.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -12.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -18.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -13.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 59.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 79.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 244 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 156 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 97.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +17.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -14.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 100 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.09× (z +10.0) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[C-33 A (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 87.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 86.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.469× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 98.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 97.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.472× (z -8.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.0861× (z -9.7) |
| [[NCI-H661 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 94.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 89.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 151 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA7]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[HADHB]] | +0.70 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[MRPS31]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CDK7]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[OGA]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SECISBP2L]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[AKAP10]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[HMGCL]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MITD1]] | +0.65 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[CIR1]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ZC2HC1A]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[TRIM23]] | +0.63 | +0.64 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.66 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.64 | -0.66 / -0.59 | both halves | 7e-06 | pathway: Cilium Assembly |
| [[MACROH2A1]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[LRP8]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.61 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[NAA15]] | -0.59 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.59 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.58 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.58 | -0.54 / -0.61 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[SLFNL1-AS1]] | -0.58 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[WDR77]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.57 | -0.47 / -0.64 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.441). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.4, -31.1); signed map (-15.2, 2.1). **Vector** length 140, 44.3% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM |  | +5.6 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +5.0 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.5 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +3.1 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -7.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -5.0 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -10.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.8 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -1.7 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -3.2 | -1.9 |
|  | [[Cinacalcet (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:55,853,648-55,905,086 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEC3, FLJ10893, BM-102, Sec3p; previously SEC3L1 |
| Gene groups (HGNC) | Exocyst complex |
| Reactome | 14 pathways, smallest: VxPx cargo-targeting to cilium; Insulin processing; Dengue virus activates/modulates innate and adaptive immune responses |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV70](https://www.uniprot.org/uniprotkb/Q9NV70) (Exocyst complex component 1):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane.; (Microbial infection) Has an antiviral effect against flaviviruses by affecting viral RNA transcription and translation through the sequestration of elongation factor 1-alpha (EEF1A1). This results in decreased viral RNA synthesis and decreased viral protein translation.

**Summary**, from NCBI Gene [55763](https://www.ncbi.nlm.nih.gov/gene/55763):

> The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of the exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex, including this protein, are found to interact with the actin cytoskeletal remodeling and …

**Accessions** — [HGNC:30380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30380) · Entrez [55763](https://www.ncbi.nlm.nih.gov/gene/55763) · UniProt [Q9NV70](https://www.uniprot.org/uniprotkb/Q9NV70) · Ensembl [ENSG00000090989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090989)

## Data

Gene col 1647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1647); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1647]; `tensor/DDL_lfc|DDL_z.npy` [1647]; `embed/gene_vectors.npy` [1647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1647 or target_col == 1647). Every well: [[EXOC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
