---
symbol: "SRP9"
type: "gene"
col: 6793
ensembl_id: "ENSG00000143742"
name: "signal recognition particle 9"
location: "1q42.12"
module: 25
arm: "+"
pooled_cpm: 88.08
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SRP9

*signal recognition particle 9* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.58× (z +20.5, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 0.05 µM: 1.18× (z +3.4, q 0.031, up in 17 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (PANC-1 2.95×, A549 3.84×, NCI-H1792 4.25×, SNU-423 3.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HT-29 3.31×, SW480 3.07×, PANC-1 2.59×, A498 2.78×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.660× (z -12.7, q 3e-34, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBX5]] (+0.73, fdr 1e-05), [[LIN7C]] (+0.72, fdr 1e-05), [[RAB1B]] (+0.70, fdr 1e-05); moves opposite to [[LINC00685]] (-0.72, fdr 7e-06), [[RPL36AL]] (-0.66, fdr 8e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[RPS27]] (-0.66, fdr 2e-05), [[SNHG7]] (-0.65, fdr 9e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6793.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (PANC-1 2.95×, A549 3.84×, NCI-H1792 4.25×, SNU-423 3.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HT-29 3.31×, SW480 3.07×, PANC-1 2.59×, A498 2.78×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +20.5 | 0e+00 | 48/49 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +20.1 | 0e+00 | 42/44 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +12.4 | 4e-33 | 41/45 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.30×** | +5.7 | 2e-06 | 33/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.26×** | +5.0 | 7e-05 | 26/48 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.24×** | +4.7 | 3e-04 | 26/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.49×** | +4.5 | 5e-04 | 24/49 (HS-578T, A498, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.23×** | +4.5 | 5e-04 | 25/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.47×** | +4.3 | 9e-04 | 31/47 (HS-578T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.20×** | +4.0 | 0.004 | 21/48 (A549, A-172, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.12× | +3.5 | 0.028 | 5/49 (SW480, KATO III, …) | rises with dose |  |
| [[NG25 (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.031 | 17/49 (LS 180, PANC-1, …) | inconsistent across doses | position effect removed |
| [[OTS514 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.031 | 18/46 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.040 | 16/48 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.065 | 13/47 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6793.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -12.7 | 3e-34 | 36/49 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.659×** | -9.0 | 6e-17 | 43/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.697×** | -7.8 | 1e-12 | 39/48 (AsPC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -7.1 | 2e-10 | 1/50 (NCI-H661) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.734×** | -6.7 | 3e-09 | 34/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.744×** | -6.4 | 2e-08 | 34/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -5.1 | 3e-05 | 21/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -4.4 | 6e-04 | 25/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -3.8 | 0.009 | 17/48 (MIA PaCa-2, SHP-77, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.883× | -3.8 | 0.009 | 13/48 (SNU-1, CHP-212, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.6 | 0.017 | 22/50 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.844× | -3.4 | 0.028 | 19/48 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 0.5 µM |  | 0.848× | -3.3 | 0.037 | 15/48 (COLO 205, C32, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 0.852× | -3.2 | 0.062 | 11/49 (HEC-1-A, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.062 | 17/48 (SHP-77, KATO III, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.857× | -3.1 | 0.062 | 17/48 (SHP-77, KATO III, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 121 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +14.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 89.2 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +14.5) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 84.1 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +14.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -18.9) |
| [[LoVo (line)]] | wt | 69.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +13.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.9) |
| [[SW 900 (line)]] | alt | 122 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.7) |
| [[SW480 (line)]] | alt | 91.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +14.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -11.8) |
| [[A549 (line)]] | wt | 73.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +16.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 74.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +13.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 98.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +13.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 82.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 65.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 90.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +15.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.629× (z -8.6) |
| [[LS 180 (line)]] | wt | 96.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +12.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 82.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 77.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 91.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.39× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 116 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +14.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 82.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -11.2) |
| [[PANC-1 (line)]] | alt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +17.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 84.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -11.5) |
| [[SNU-423 (line)]] | alt | 76.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 80.0 | 0 | 3 (1 ⚠) | — | [[Cilostazol (drug)]] 5 µM 0.0774× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 96.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.9) |
| [[H4 (line)]] | wt | 93.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 72.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 97.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -12.0) |
| [[KATO III (line)]] | alt | 79.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +12.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 73.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 64.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +15.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 76.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 72.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 74.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.1) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.477× (z -8.7) |
| [[SW 1271 (line)]] | alt | 73.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0741× (z -10.9) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Pyridoxine (drug)]] 0.5 µM 0.123× (z -8.6) |
| [[A-427 (line)]] | wt | 72.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 85.1 | 0 | 1 | — | [[GSK1059615 (drug)]] 5 µM 0.0722× (z -9.0) |
| [[C-33 A (line)]] | alt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.5) |
| [[CHP-212 (line)]] | wt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.3) |
| [[COLO 205 (line)]] | alt | 97.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.4) |
| [[HCT15 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 76.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 59.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 73.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 87.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX5]] | +0.73 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.72 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[RAB1B]] | +0.70 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[ALG10]] | +0.70 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[TMEM237]] | +0.69 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.68 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[MBTPS2]] | +0.67 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[VMA21]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MRPL42]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[OCRL]] | +0.65 | +0.36 / +0.70 | both halves | 1e-04 |  |
| [[CAPRIN1]] | +0.64 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[MAD2L1]] | +0.64 | +0.70 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 9 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00685]] | -0.72 | -0.58 / -0.77 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | -0.66 | -0.37 / -0.76 | both halves | 8e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 864; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27]] | -0.66 | -0.48 / -0.72 | both halves | 2e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 856 |
| [[SNHG7]] | -0.65 | -0.57 / -0.72 | both halves | 9e-06 |  |
| [[ZFAS1]] | -0.65 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[SNHG19]] | -0.65 | -0.47 / -0.74 | both halves | 2e-05 |  |
| [[MSX1]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[RPS19]] | -0.65 | -0.46 / -0.72 | both halves | 3e-05 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 856 |
| [[SNHG6]] | -0.64 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[DNLZ]] | -0.64 | -0.38 / -0.66 | both halves | 7e-05 |  |
| [[C1orf122]] | -0.64 | -0.39 / -0.70 | both halves | 5e-05 |  |
| [[COMMD6]] | -0.64 | -0.37 / -0.78 | both halves | 8e-05 |  |
| [[EPB41L4A-AS1]] | -0.64 | -0.59 / -0.68 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SRP9's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.1, -18.7); signed map (-16.3, -39.2). **Vector** length 93.7, 23.9% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +20.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +20.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.9 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +2.8 | +5.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | -3.1 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.2 | -0.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | signal recognition particle 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:225,777,813-225,790,468 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Signal recognition particle |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P49458](https://www.uniprot.org/uniprotkb/P49458) (Signal recognition particle 9 kDa protein):

> Component of the signal recognition particle (SRP) complex, a ribonucleoprotein complex that mediates the cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER) (By similarity). SRP9 together with SRP14 and the Alu portion of the SRP RNA, constitutes the elongation arrest domain of SRP. The complex of SRP9 and SRP14 is required for SRP RNA binding (By similarity).

**Summary**, from NCBI Gene [6726](https://www.ncbi.nlm.nih.gov/gene/6726):

> Predicted to enable RNA binding activity and signal recognition particle binding activity. Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane. Predicted to be located in cytosol. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11304) · Entrez [6726](https://www.ncbi.nlm.nih.gov/gene/6726) · UniProt [P49458](https://www.uniprot.org/uniprotkb/P49458) · Ensembl [ENSG00000143742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143742)

## Data

Gene col 6793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6793); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6793]; `tensor/DDL_lfc|DDL_z.npy` [6793]; `embed/gene_vectors.npy` [6793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6793 or target_col == 6793). Every well: [[SRP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
