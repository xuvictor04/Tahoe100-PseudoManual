---
symbol: "MACROD2"
type: "gene"
col: 10231
ensembl_id: "ENSG00000172264"
name: "mono-ADP ribosylhydrolase 2"
location: "20p12.1"
module: 8
arm: "+"
pooled_cpm: 109.81
n_lines_expressing: 40
n_dd_up: 30
n_dd_down: 40
n_dd_up_clean: 27
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MACROD2

*mono-ADP ribosylhydrolase 2* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +11.3, q 6e-27, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (14 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.426× (z -10.7, q 4e-24, down in 36 of 38 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.442× (z -10.7, q 4e-24, down in 35 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WWOX]] (+0.59, fdr 1e-05), [[TBL1XR1]] (+0.56, fdr 4e-05), [[MPP7]] (+0.53, fdr 2e-05); moves opposite to [[GMIP]] (-0.54, fdr 3e-05), [[EP400P1]] (-0.53, fdr 4e-05), [[AGAP5]] (-0.50, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +11.3 | 6e-27 | 33/38 (A498, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +8.0 | 3e-13 | 30/38 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +7.5 | 1e-11 | 32/38 (KATO III, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +7.3 | 5e-11 | 26/38 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +7.2 | 7e-11 | 29/39 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +6.6 | 3e-09 | 30/38 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +6.0 | 1e-07 | 25/38 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 2e-05 | 28/38 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +5.1 | 2e-05 | 23/38 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 7e-05 | 28/38 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 4e-04 | 29/39 (BT-474, HCT15, …) | two highest doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +4.4 | 6e-04 | 21/39 (LoVo, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.26×** | +4.4 | 6e-04 | 21/38 (A-427, KATO III, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.86×** | +4.3 | 8e-04 | 24/39 (BT-474, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +4.1 | 0.002 | 24/38 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.78×** | +4.0 | 0.002 | 24/40 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.426×** | -10.7 | 4e-24 | 36/38 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.442×** | -10.7 | 4e-24 | 35/38 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -10.1 | 7e-22 | 38/38 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.462×** | -10.1 | 8e-22 | 35/38 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -9.9 | 5e-21 | 35/38 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.470×** | -9.9 | 5e-21 | 33/38 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.510×** | -8.8 | 1e-16 | 34/38 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.307×** | -8.1 | 4e-14 | 36/38 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.309×** | -8.0 | 5e-14 | 38/39 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -7.9 | 1e-13 | 31/38 (HEC-1-A, PANC-1, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.560×** | -7.6 | 2e-12 | 33/38 (HT-29, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.576×** | -6.9 | 2e-10 | 29/38 (SNU-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.703×** | -6.5 | 4e-09 | 23/38 (NCI-H23, HEC-1-A, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.582×** | -6.4 | 7e-09 | 33/38 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.639×** | -5.8 | 2e-07 | 30/38 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -5.2 | 6e-06 | 24/38 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -5.2 | 6e-06 | 27/38 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.774×** | -4.7 | 7e-05 | 29/39 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.567×** | -3.9 | 0.003 | 24/38 (HT-29, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.746×** | -3.8 | 0.003 | 23/38 (HT-29, LoVo, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.009 | 22/39 (HT-29, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 324 | 0 | 17 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0110× (z -36.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.126× (z -17.6) |
| [[HEC-1-A (line)]] | alt | 637 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -18.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -14.0) |
| [[C32 (line)]] | wt | 684 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -13.8) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 392 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -16.5) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.111× (z -10.1) |
| [[HT-29 (line)]] | alt | 113 | 0 | 10 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -12.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.269× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 160 | 1 (1 ⚠) | 9 (6 ⚠) | [[Selinexor (drug)]] 5 µM 2.21× (z +8.9) ⚠ cell-cycle shift, explains ~77% of this change | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -19.1) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.171× (z -14.1) |
| [[PANC-1 (line)]] | alt | 55.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.8) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.8) |
| [[A549 (line)]] | wt | 84.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.8) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.200× (z -10.6) |
| [[KATO III (line)]] | alt | 145 | 5 (1 ⚠) | 1 | [[Ponatinib (drug)]] 5 µM 3.86× (z +11.5) | [[Ixazomib citrate (drug)]] 5 µM 0.290× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 80.7 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.40× (z +10.0) | [[Digitoxin (drug)]] 0.05 µM 0.308× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.344× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 91.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.5) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -9.9) |
| [[A-172 (line)]] | wt | 48.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 150 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -12.4) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -8.5) |
| [[HS-578T (line)]] | alt | 165 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.270× (z -10.0) |
| [[LoVo (line)]] | wt | 98.0 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.29× (z +9.8) | [[Ixazomib citrate (drug)]] 5 µM 0.289× (z -10.5) |
| [[A498 (line)]] | wt | 72.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.09× (z +13.7) | — |
| [[HOP62 (line)]] | alt | 55.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +10.1) | — |
| [[J82 (line)]] | alt | 77.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.315× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 52.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.27× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 263 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -9.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.195× (z -9.1) |
| [[A-427 (line)]] | wt | 71.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.79× (z +15.3) ⚠ cell-cycle shift, explains ~77% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.197× (z -12.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.291× (z -9.1) |
| [[HCT15 (line)]] | alt | 112 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -10.4) |
| [[SW 1271 (line)]] | alt | 65.8 | 0 | 2 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0575× (z -9.0) ⚠ transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0617× (z -8.8) |
| [[SW480 (line)]] | alt | 43.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 226 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.247× (z -11.5) |
| [[CHP-212 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -11.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 71.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.216× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 97.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 42.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.67× (z +10.5) | — |
| [[RKO (line)]] | wt | 36.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.03× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.91× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 103 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.190× (z -9.5) |
| [[AN3 CA (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 25.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 24.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WWOX]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 | STRING 513 |
| [[TBL1XR1]] | +0.56 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[MPP7]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[CPVL]] | +0.50 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[USP9X]] | +0.49 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[ADGRV1]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SCN9A]] | +0.48 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[AGBL4]] | +0.48 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[DAB1]] | +0.48 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RERG]] | +0.48 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PBX1]] | +0.48 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[DCDC2]] | +0.48 | +0.46 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMIP]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[EP400P1]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[AGAP5]] | -0.50 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[C10orf88]] | -0.49 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[TAF12]] | -0.46 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[ELMOD3]] | -0.44 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[TRAPPC12]] | -0.44 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[MRPS11]] | -0.44 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[GOSR2]] | -0.43 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[LPAR2]] | -0.43 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[GON4L]] | -0.43 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[PRKAG1]] | -0.42 | -0.40 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.211). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.4, 33.9); signed map (48.4, 1.5). **Vector** length 92.8, 29.1% of its response variance represented; |z| ≥ 3 in 1,514 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | +5.1 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +7.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.4 | -10.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.2 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -3.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -2.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | mono-ADP ribosylhydrolase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:13,995,369-16,053,197 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ631M13.5; previously C20orf133 |
| Gene groups (HGNC) | Macro domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A1Z1Q3](https://www.uniprot.org/uniprotkb/A1Z1Q3) (ADP-ribose glycohydrolase MACROD2):

> Removes ADP-ribose from aspartate and glutamate residues in proteins bearing a single ADP-ribose moiety. Inactive towards proteins bearing poly-ADP-ribose. Deacetylates O-acetyl-ADP ribose, a signaling molecule generated by the deacetylation of acetylated lysine residues in histones and other proteins.

**Summary**, from NCBI Gene [140733](https://www.ncbi.nlm.nih.gov/gene/140733):

> The protein encoded by this gene is a deacetylase involved in removing ADP-ribose from mono-ADP-ribosylated proteins. The encoded protein has been shown to translocate from the nucleus to the cytoplasm upon DNA damage. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:16126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16126) · Entrez [140733](https://www.ncbi.nlm.nih.gov/gene/140733) · UniProt [A1Z1Q3](https://www.uniprot.org/uniprotkb/A1Z1Q3) · Ensembl [ENSG00000172264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172264)

## Data

Gene col 10231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10231); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10231]; `tensor/DDL_lfc|DDL_z.npy` [10231]; `embed/gene_vectors.npy` [10231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10231 or target_col == 10231). Every well: [[MACROD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MACROD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
